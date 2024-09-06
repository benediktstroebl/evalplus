
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
    if txt.count(" ") > 0:
        return txt.split()
    elif txt.count(",") > 0:
        return txt.split(",")
    else:
        res = 0
        for i in range(26):
            if chr(ord("a")+i) in txt and (ord(chr(ord("a")+i)) + 1) % 2 != 0:
                res += 1
        return res

