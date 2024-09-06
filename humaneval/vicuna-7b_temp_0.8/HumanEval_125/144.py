
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
    txt = txt.lower() # convert text to lower case
    txt = txt.split() # split on whitespace
    if txt: # if txt is not empty
        txt = txt[0] # take the first element of the list
        if txt.endswith(','): # check if the first element ends with a comma
            txt = txt[:-1] # remove the last comma
        if txt.count(' ') == 0: # if txt has no whitespaces
            txt = [ord(c) for c in txt] # convert txt to a list of characters and their corresponding ordinal values
            for i, c in enumerate(txt):
                if c.isalpha() and (i % 2 == 1): # check if the ordinal of c is odd
                    txt.insert(i, ' ') # insert a space in the appropriate position
            txt = ' '.join(txt) # join the list of characters with spaces
        else: # if txt has whitespaces
            txt = txt.replace(' ', ',') # replace whitespaces with commas
    return txt