
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
    # if not txt.split(): return len([word for word in txt if ord(word) % 2!= 0])
    # if not txt.split(","): return len([word for word in txt if ord(word) % 2!= 0])
    return txt.split() if txt.split() else txt.split(",")

