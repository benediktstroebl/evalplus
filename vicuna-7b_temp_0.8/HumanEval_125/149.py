
def split_words(txt):
    '''
    Given a string of words, return a list of words split on whitespace, if no whitespaces exists in the text you
    should split on commas ',' if no commas exists you should return the number of lower-case letters with odd order in the
    alphabet, ord('a') = 0, ord('b') = 1, ... ord('z') = 25
    Examples
    split_words("Hello world!") ➞ ["Hello", "world!"]
    split_words("Hello,world!") ➞ ["Hello", "world!"]
    split_words("abcdef") == 3 
    '''
    txt = txt.lower() # To make all letters lowercase
    txt = txt.split() # To split on whitespace
    txt = txt.replace(',', ' ') # To replace commas with spaces
    txt = txt.replace('  ', ' ') # To replace multiple spaces with single spaces
    txt = txt.replace('\n', ' ') # To replace newline with space
    txt = txt.replace('\t', ' ') # To replace tabulation with space
    txt = txt.replace('  ', ' ') # To replace multiple spaces with single spaces
    txt = txt.replace('%', ' ') # To replace percentage sign with space
    txt = txt.replace('$', ' ') # To replace dollar sign with space
    txt = txt.replace('%', ' ') # To replace percentage sign with space
    txt = txt.replace('$', ' ') # To replace dollar sign with space
    txt = txt.split(' ') # To split on spaces
    txt = txt.split(',') # To split on commas
    txt = txt.split('%') # To split on percentage sign
    txt = txt.split('$') # To split on dollar sign
    txt = txt.split('\n') # To split on newline
    txt = txt.split('\t') # To split on tabulation
    if txt: # Check if the text is not empty
        txt = txt.split() # To split on any whitespace
        txt = txt.split() # To split on any whitespace
        txt = txt.split() # To split on any whitespace
        txt = txt.split() # To split on any whitespace
        txt = txt.split() # To split on any whitespace
        txt = txt.split() # To split on any whitespace
        txt = txt.split() # To split on any whitespace
        txt = txt.split() # To split on any whitespace
        txt = txt.split() # To split on any whitespace
        txt = txt.split() # To split on any whitespace
        txt = txt.split() # To split on any whitespace
        txt = txt.split() # To split on any whitespace
        txt = txt.split() # To split on any whitespace
        txt = txt.split() # To split on any whitespace
        txt = txt.split() # To
