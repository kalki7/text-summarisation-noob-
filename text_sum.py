import nltk
from nltk.tokenize import RegexpTokenizer, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
import operator
import matplotlib.pyplot as plt

stopwords = stopwords.words('english')

tokenizer = RegexpTokenizer(r'\w+')

stemmer = SnowballStemmer('english')

f1 = open('text_file.txt')

text1 = f1.read()

tk1 = nltk.Text(tokenizer.tokenize(text1))

tk1 = [w.lower() for w in tk1 if w.isalpha() and not w.isdigit()]

tk1 = [stemmer.stem(w) for w in tk1 if w not in stopwords]

index1 = nltk.FreqDist(tk1)

comb = index1.keys()
cindex = nltk.FreqDist(comb)

sent1 = sent_tokenize(text1)


t1 = 'text_file.txt'

title1 = [stemmer.stem(w.lower()) for w in tokenizer.tokenize(t1) if w.isalpha() and w not in stopwords]

scores1 = {}
sentence_lengths = []
for sentence in sent1:
	sentence_lengths.append(len(sentence))
	if len(sentence) < 81:
		# OWN - find all words in the sentence
		words = tokenizer.tokenize(sentence)
		words = [stemmer.stem(w.lower()) for w in words if w.isalpha() and not w.isdigit()]


		score = 0.0
		titlewords = 0.0
		for word in words:
			score = score + index1[word] / (1+cindex[word])
			if word in title1:
				titlewords += 1


		titlewords = 0.1 * titlewords / len(title1)
		scores1[sentence] = score + titlewords


print ('text_file.txt')
for sentence in scores1.keys():
	if scores1[sentence] >= 9:
		print (sentence)
