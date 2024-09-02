
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
    if txt == "":
        return txt
    if txt.split().__len__() == 0:
        if txt.find(',') > -1:
            return txt.split(',')
        else:
            return sum(1 for c in txt if ord(c) < 122 and ord(c) % 2 != 0)
    return txt.split()


