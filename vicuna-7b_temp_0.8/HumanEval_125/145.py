
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
    txt = txt.lower() # converting to lowercase
    txt = txt.split() # splitting on whitespaces
    if txt: # check if the txt has any whitespaces
        txt = txt.split(',') # splitting on commas if whitespaces exists
    if txt: # check if the txt has any commas
        words = txt.split() # splitting on whitespaces
        return words
    else:
        return len(set(txt)) // 2 # returning the number of lower-case letters with odd order in the alphabet
