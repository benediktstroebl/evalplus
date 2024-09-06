
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
    txt = txt.lower()
    if not txt:
        return 0
    txt = txt.split()
    if not txt:
        return 0
    txt = [txt[0] if txt[0] == ',' else txt[0] for txt in txt]
    txt = [txt[0] for txt in txt]
    if len(txt) > 1:
        return txt[0]
    else:
        return txt[0].count('a') + txt[0].count('b') + txt[0].count('c') + txt[0].count('d') + txt[0].count('e') + txt[0].count('f')
