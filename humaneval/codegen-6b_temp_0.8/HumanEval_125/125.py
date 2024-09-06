
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
    # a = txt.split(' ')
    # b = ''.join(a)
    # c = b.split(',')
    # d = ''.join(c)
    # e = d.split(' ')
    # f = ''.join(e)
    # g = f.lower()
    # h = len(g)
    # if h % 2 == 1:
    #     return h
    # else:
    #     return 'None'

    return len(txt.replace(' ','').lower()) % 2 == 1

