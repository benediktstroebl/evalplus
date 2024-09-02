
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
    lst = []
    if txt.find(' ') == -1:
        if txt.find(',') == -1:
            return len([ch for ch in txt if ch.isalpha() if ord(ch) % 2])
        else:
            for x in txt.split(','):
                lst.append(x)
            return lst
    else:
        for x in txt.split():
            lst.append(x)
        return lst
    

