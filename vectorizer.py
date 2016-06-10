
# coding: utf-8

# In[ ]:

import os
import pickle
import re
import sys


# The list of all the emails from Sara are in the `from_sara` list likewise for emails from Chris (`from_chris`).
# The actual documents are in the Enron email dataset, which you downloaded/unpacked. The data is stored in lists and packed away in pickle files at the end.

# In[ ]:

from_sara  = open('../text_learning/from_sara.txt', "r")
from_chris = open('../text_learning/from_chris.txt', "r")

from_data = []
word_data = []


# In[ ]:

from nltk.stem.snowball import SnowballStemmer
import string

filePath = '/Users/omojumiller/mycode/hiphopathy/HipHopDataExploration/JayZ/'

f = open(filePath+"JayZ_American Gangster_American Gangster.txt", "r")
f.seek(0)  ### go back to beginning of file (annoying)
all_text = f.read()

content = all_text.split("X-FileName:")
words = ""
stemmer = SnowballStemmer("english")
text_string = content
for sentence in text_string:
    words = sentence.split()
    
stemmed_words = [stemmer.stem(word) for word in words]


# In[ ]:

def parseOutText(f):
    """ given an opened email file f, parse out all text below the
        metadata block at the top
        
        example use case:
        f = open("email_file_name.txt", "r")
        text = parseOutText(f)
        
        """

    stemmer = SnowballStemmer("english")
    
    f.seek(0)  ### go back to beginning of file (annoying)
    all_text = f.read()

    ### split off metadata
    content = all_text.split("X-FileName:")
    words = ""
    if len(content) > 1:
        ### remove punctuation
        text_string = content[1].translate(string.maketrans("", ""), string.punctuation)

        ### split the text string into individual words, stem each word,
        ### and append the stemmed word to words (make sure there's a single
        ### space between each stemmed word)
        
        words = ' '.join([stemmer.stem(word) for word in text_string.split()])
        
    return words


# In[ ]:

ff = open("../text_learning/test_email.txt", "r")
text = parseOutText(ff)
#print text


# `temp_counter` is a way to speed up the development--there are thousands of emails from Sara and Chris, so running over all of them can take a long time. `temp_counter` helps you only look at the first 200 emails in the list so you can iterate your modifications quicker

# In[ ]:

temp_counter = 1

print "processing emails"

for name, from_person in [("sara", from_sara), ("chris", from_chris)]:   
    for path in from_person:
        
        ### only look at first 200 emails when developing
        ### once everything is working, remove this line to run over full dataset
        
        #temp_counter += 1
        
        
        if temp_counter:
            path = os.path.join('..', path[:-1])
            #print path
            email = open(path, "r")

            ### use parseOutText to extract the text from the opened email
            text = parseOutText(email)

            ### use str.replace() to remove any instances of the words
            replaceWords = ["sara", "shackleton", "sshacklensf", "cgermannsf", "chris", "germani"]
            for word in replaceWords:
                text = text.replace(word, '')
                

            ### append the text to word_data
            word_data.append(text)

            ### append a 0 to from_data if email is from Sara, and 1 if email is from Chris
            if name == "sara": 
                from_data.append(0)
            else:
                from_data.append(1)
                

            email.close()

print "emails processed"
from_sara.close()
from_chris.close()

pickle.dump( word_data, open("your_word_data.pkl", "w") )
pickle.dump( from_data, open("your_email_authors.pkl", "w") )




