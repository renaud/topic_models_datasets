topic_models_datasets
=====================

Some datasets for topic modelling.

### LDA-C format:

    [M] [term_1]:[count] [term_2]:[count] ...  [term_N]:[count]

where `[M]` is the number of unique terms in the document, and the
`[count]` associated with each term is how many times that term appeared
in the document.

---------

To reconstruct a view from the original document, a python script is provided:

    python view_corpus.py test/corpus1.lda-c test/corpus1.lda-c.vocab

---------

### Genia

- [source](http://www.nactem.ac.uk/genia/genia-corpus/term-corpus)
- 2000 Pubmed abstracts
- processing:
	- lemmatization: BioLemmatizer
	- stopwords: mallet_stopwords_en.txt
	- punctuation removed
- vocabulary size: 21790

### 20 newsgroups
- [source](qwone.com/~jason/20Newsgroups/20news-19997.tar.gz)
- preprocessing_1
(pipelines/projects/preprocessing/20131014_preprocess_corpus_to_lda-c/20131121_20ng.pipeline)
    - BioLemmatizer
    - StopwordFilter
    - PunctuationFilter
- preprocessing_2
(modules/blue_uima/src/test/java/ch/epfl/bbp/uima/projects/misc/Preprocess20NG.java)
    - RegexTokenizerAnnotator
      - Splits on any punctuation character, except dashes
      - `(?<=[(a-zA-Z_0-9\\-)])(?=[^(a-zA-Z_0-9\\-)])|(?<=[^(a-zA-Z_0-9\\-)])(?=[(a-zA-Z_0-9\\-)])`
    - Punctuation
    - SnowballStemmer
    - Stopwords
      - list from Mallet
    - BlackList
      - `%)(.,;!?\"_>","<#^:/\\=-+*$@[]&{}|`
      - numbers (0 to 9)
- preprocessing_3
  N.A.

## KTH
- [source](http://www.csc.kth.se/~chengz/KTH.tar.gz)
- author: Cheng Zhang

### test
- synthetic corpus of 3 documents, for unit testing
