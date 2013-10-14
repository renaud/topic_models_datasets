topic_models_datasets
=====================

Some datasets for topic modelling.

### LDA-C format:

    [M] [term_1]:[count] [term_2]:[count] ...  [term_N]:[count]

where `[M]` is the number of unique terms in the document, and the
`[count]` associated with each term is how many times that term appeared
in the document. 

---------

### Genia

- [source](http://www.nactem.ac.uk/genia/genia-corpus/term-corpus)
- 2000 Pubmed abstracts
- processing:
	- lemmatization: BioLemmatizer
	- stopwords: mallet_stopwords_en.txt
	- punctuation removed
- vocabulary size: 21790 