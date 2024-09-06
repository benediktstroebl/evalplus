
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
    
    if txt.find(' '):
        return txt.split(' ')
    elif txt.find(','):
        return txt.split(',')
    else:
        a = []
        for i in range(len(txt)):
            a.append(chr(ord('a') + i))
        return len([i for i in a if ord(i)%2 == 1])
