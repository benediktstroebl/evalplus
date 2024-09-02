
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
    a = txt.split()
    b = txt.split(",")
    c = [ord(char) for char in txt.lower() if ord(char) % 2 == 1]
    d = len(c)
    return a if len(a) > 0 else b if len(b) > 0 else d

