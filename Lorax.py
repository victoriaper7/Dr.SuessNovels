import random
from textblob import TextBlob
import nltk
nltk.download ('punkt')

nltk.download('averaged_perception_tagger')
import glob

from textblob import TextBlob

with open("/content/Lorax.txt") as f:
    text = f.read()                     
    textBlb = TextBlob(text)
    textCorrected = textBlb.correct()
    print(textCorrected)
    
    with open("/content/Lorax.txt", errors="surrogateescape") as f:
  text = f.read()

blob = TextBlob(text)

all_of_the_words = blob.words

# count the words:
len(all_of_the_words)

"Lorax" in all_of_the_words

# iterate through the list of words
# when a word is "Truffula" print whatever word comes next
for i in range(len(all_of_the_words)):
  if (all_of_the_words[i] == "Truffula"):
    print(all_of_the_words[i + 1])
    
    
    >>> b = TextBlob("grickle, Lorax, Lerkim, once-ler, miff-muffered moff")
>>> print(b.correct())


>>> from textblob import Word
>>> w = Word('Thneed')
>>> w.spellcheck()
[('Thneed', 1.0)]


import nltk
nltk.download('averaged_perceptron_tagger')


# get a list of all the foreign words
for word, pos in blob.tags:
  if (pos == "FW"):
    print(word) 
    
    
 # get a list of all the Adjectives
# These are most of the "pretent" words from The Lorax
for word, pos in blob.tags:
  if (pos == "JJ"):
    print(word)
    
    
 # get a list of all the adjective, comparatives
for word, pos in blob.tags:
  if (pos == "JJR"):
    print(word)
    
 # get a list of all the NN-noun, singular 
for word, pos in blob.tags:
  if (pos == "NN"):
    print(word)
    
 # get a list of all the CC-coordinating conjunction
for word, pos in blob.tags:
  if (pos == "CC"):
    print(word)
    
 # get a list of all the RBR-adverb, comparative better
for word, pos in blob.tags:
  if (pos == "RBR"):
    print(word)
