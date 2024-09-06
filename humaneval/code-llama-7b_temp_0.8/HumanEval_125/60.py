
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
    if len(txt) == 0:
        return []
    
    words = []
    txt = txt.strip()
    i = 0
    while i < len(txt):
        while i < len(txt) and txt[i] != ' ' and txt[i] != ',':
            i += 1
        if i < len(txt) and txt[i] == ',':
            words.append(txt[:i])
            txt = txt[i+1:]
            i = 0
        elif i < len(txt):
            words.append(txt[:i])
            txt = txt[i+1:]
            i = 0
    return words


