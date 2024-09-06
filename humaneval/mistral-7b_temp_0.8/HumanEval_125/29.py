
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
    arr = txt.split(' ')
    res = []
    if len(arr) == 0:
        a = list(txt.lower())
        res = [ord(x) for x in a if x.isalpha() and x.islower()]
        return res
    else:
        for x in arr:
            if len(x.split(',')) == 0:
                a = list(x.lower())
                res = [ord(x) for x in a if x.isalpha() and x.islower()]
                return res
            else:
                a = x.split(',')
                res = a
                return res

