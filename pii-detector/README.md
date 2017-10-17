Step 1. Download stanford-ner from https://nlp.stanford.edu/software/CRF-NER.shtml#Download.

Step 2. Launch it using `java -mx1500m -cp stanford-ner.jar edu.stanford.nlp.ie.NERServer  -loadClassifier classifiers/english.muc.7class.distsim.crf.ser.gz  -port 8080 -outputFormat inlineXML`

<h2>About Stanford-NER</h2>

Stanford NER is a Java implementation of a Named Entity Recognizer. Named Entity Recognition (NER) labels sequences of words in a text which are the names of things, such as person and company names, or gene and protein names. It comes with well-engineered feature extractors for Named Entity Recognition, and many options for defining feature extractors. Included with the download are good named entity recognizers for English, particularly for the 3 classes (PERSON, ORGANIZATION, LOCATION), and we also make available on this page various other models for different languages and circumstances, including models trained on just the CoNLL 2003 English training data.
