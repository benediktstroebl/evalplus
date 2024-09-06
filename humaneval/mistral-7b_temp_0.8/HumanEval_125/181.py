
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
    try:
        res = txt.split()
    except:
        res = []
        for i in txt:
            if i == ',':
                res.append(' ')
            else:
                res.append(i)
    res = list(filter(lambda x:x.lower().isalpha(),res))
    res = sorted([i.lower() for i in res])
    return [i for i in res if i.islower() and i[1]%2==0]
