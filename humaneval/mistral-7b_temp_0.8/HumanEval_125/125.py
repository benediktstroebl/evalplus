
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
    s = txt.split()
    if len(s) > 0:
        return s
    else:
        l = len(txt)
        w = 0
        for c in txt:
            if c.isalpha():
                if ord(c) % 2 != 0:
                    w += 1
        return w
