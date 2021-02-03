#%%
import re
import os
import pathlib

NOTBOOKS = pathlib.Path('notebooks')
SCRIPTS = pathlib.Path("scripts")

if os.path.exists(NOTBOOKS): 
    os.system(f"rm -r {NOTBOOKS}")
    NOTBOOKS.mkdir()
if os.path.exists(SCRIPTS): 
    os.system(f"rm -r {SCRIPTS}")
    SCRIPTS.mkdir()

os.system("wget -O code.R https://raw.githubusercontent.com/rmcelreath/rethinking/master/book_code_boxes.txt")


with open("code.R") as f:
    code = [ l for l in f ]


def append_rscript(path, line):
    with open(path, "a", encoding="utf-8") as f:
        f.write(line)


pat_codenum = re.compile(r'^## R code (\d{1,2})\.(\d{1,3})')
curr_chap = 0
curr_file = f"ch{curr_chap:02}.R"

for line in code:
    if line.startswith("## R code"):
        codenum = pat_codenum.search(line)
        if codenum != None:
            chap, num = int(codenum[1]), int(codenum[2])

        if chap > curr_chap:
            curr_chap = chap
            curr_file = f"ch{curr_chap:02}.R"
            append_rscript(SCRIPTS / curr_file, "#+ Setup \nremotes::install_github('rmcelreath/rethinking', upgrade=F)\n\n")

        append_rscript(SCRIPTS / curr_file, line.replace("## R code", "#' R code"))
        append_rscript(SCRIPTS / curr_file, line.replace("## R code", "#+ R code"))
    else:
        append_rscript(SCRIPTS / curr_file, line)


# Convert to Notebooks
for fp in SCRIPTS.glob("*.R"):
    os.system(f'''Rscript -e "knitr::spin('{fp}',knit=F)"''')
    rmd_path = str(fp).replace(".R", ".Rmd")
    os.system(f"jupytext --to notebook {rmd_path}")
os.system(f"mv {SCRIPTS}/*.ipynb {NOTBOOKS}")
# %%
