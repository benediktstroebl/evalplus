
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
    # 1st approach
    # return txt.split() if ' ' in txt else ord('a')
    # 2nd approach
    # return txt.split() if ' ' in txt else [str(ord(txt[i]) - ord('a') + 1) for i in range(len(txt)) if ord(txt[i]) - ord('a') < 26]
    # 3rd approach
    # if ' ' in txt:
    #     return txt.split()
    # elif ',' in txt:
    #     return txt.split(',')
    # else:
    #     return [str(ord(txt[i]) - ord('a') + 1) for i in range(len(txt)) if ord(txt[i]) - ord('a') < 26]
    # 4th approach
    if ' ' in txt:
        return txt.split()
    elif ',' in txt:
        return txt.split(',')
    else:
        return [txt[i] for i in range(len(txt)) if ord(txt[i]) - ord('a') < 26]

