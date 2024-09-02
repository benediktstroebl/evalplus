
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
    # res = txt.split(' ')
    # if ' ' not in txt:
    #     return ','.join(txt.split(','))
    # return res

    if ' ' in txt:
        res = txt.split(' ')
        return res
    if ',' in txt:
        res = txt.split(',')
        return res
    return len([i for i in txt.lower() if i.isalpha() and i.lower() in "abcdefghijklmnopqrstuvwxyz" and ord(i) % 2 != 0])

