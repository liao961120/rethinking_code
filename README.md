# Code boxes in Statistical Rethinking

This repo contains the [code boxes](https://github.com/rmcelreath/rethinking/blob/master/book_code_boxes.txt) in the book [Statistical Rethinking](https://xcelab.net/rm/statistical-rethinking/), converted to `.ipynb`, making it convenient to load the code into Kaggle's [Notebook environment](https://www.kaggle.com/docs/notebooks) (it's free).


## Why

The `rethinking` R package requires `rstan`, which is not easy to install and may cause problems on some computers. [Kaggle's R notebook has Rstan installed already](https://stackoverflow.com/questions/63116262/how-to-open-a-new-google-colab-notebook-for-r#answer-63116319), thus making the setup of the environment fast and easy (you only need to install `rethinking` from github, which can be done by just running the first code chunk in the notebooks).


## Usage

The code from [`book_code_boxes.txt`](https://github.com/rmcelreath/rethinking/blob/master/book_code_boxes.txt) is split into several notebooks by chapter, which can be found in [/notebooks](./notebooks).

You can load a notebook in this repo into Kaggle's Notebook environment by clicking `File > Load from URL` in the notebook interface (also, make sure to set the language to R on the right panel). The URL is in the form of:

```
https://raw.githubusercontent.com/liao961120/rethinking_code/main/notebooks/ch{dd}.ipynb
```

So, for instance, if you want to load the [code in chapter 4](./notebooks/ch04.ipynb), the URL would be:

```
https://raw.githubusercontent.com/liao961120/rethinking_code/main/notebooks/ch04.ipynb
```
