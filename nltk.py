
# coding: utf-8

# In[10]:

from nltk.stem import PorterStemmer
ps = PorterStemmer()
e = ["python", "pythoner", "pyhtoning"]
for w in e:
    print(ps.stem(w))
s = "hello Brian"
s1 = nltk.word_tokenize(s)
print(s1)
print(nltk.pos_tag(s1))
    


# In[17]:

from nltk.stem import WordNetLemmatizer
lemmatizer  = WordNetLemmatizer()
print(lemmatizer.lemmatize("better", pos = "a"))


# In[18]:

import nltk
print(nltk.__file__)


# In[19]:

import cv2
print(cv2.__file__)


# In[24]:

from nltk.corpus import indian
from nltk.tokenize import sent_tokenize
sample = indian.raw("hindi.pos")
t = sent_tokenize(sample)
print(t[:4])


# In[26]:

from nltk.corpus import wordnet
syns = wordnet.synsets("program")
print(syns)


# In[ ]:



