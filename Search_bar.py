#Python search bar using Redis as a datastore server.

import math 
import collections
import os
import re
import redis
import unittest

NON_Word = re.compile("[a-z0-9' ]")

STOP_WORDS = set('''a able about across after all almost also am among
an and any are as at be because been but by can cannot could dear did
do does either else ever every for from get got had has have he her
hers him his how however i if in into is it its just least let like
likely may me might most must my neither no nor not of off often on
only or other our own rather said say says she should since so some
than that the their them then there these they this tis to too twas us
wants was we were what when where which while who whom why will with
would yet you your'''.split())

class scoredIndexSearch(object):
    def __init__(self, prefix, *redis_settings):
        self.prefix = prefix.lower().rstrip(':') + ':'

        #connection to redis server
        self.connection = redis.Redis(*redis_settings)
  
    @staticmethod
    def get_index_key(content, add=True):
   # Very simple word-based parser.  We skip stop words and single
        # character words.
     words = NON_Word.sub('',content.lower()).split()
     words =[words.strip("'") for word in words]
     words = [word for word in words
            if word not in NON_Word and len(word) > 1  ]
     
       # Apply the Porter Stemmer here if you would like that functionality.

        # Apply the Metaphone/Double Metaphone algorithm by itself, or after
        # the Porter Stemmer.
     if not add:
       return words
    # Calculate the TF portion of TF/IDF.
     counts = collections.defaultdict(float)
     for word in words:
        counts[words] +=1
     wordcount= len(words)
     tf = dict((word ,count / wordcount)
            for word, count in counts.iteritems()   )
     
     return tf
def _handle_content(self, id, content, add=True):
   # Get the keys we want to index.
   Keyes = self.get_index_keys(content)
   prefix = self.prefix

    # Use a non-transactional pipeline here to improve performance.
   pipe = self.connection.pipeline(False)

    # Since adding and removing items are exactly the same, except
        # for the method used on the pipeline, we will reduce our line
        # count.
   if add:

   
