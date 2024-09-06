
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
    if txt is None or txt == "":
        return []
    txt = txt.lower()
    txt = txt.split()
    txt = [txt[0] if txt[0] == txt[-1] else txt[1] for txt in txt]
    txt = [txt[i:i+2] for i in range(0, len(txt), 2)]
    txt = [txt[i:i+1] for i in range(0, len(txt), 1)]
    txt = txt[::-1]
    txt = txt[::-1].split(',')
    txt = txt[::-1].split()
    txt = [txt[i:i+1] for i in range(0, len(txt), 1)]
    txt = [txt[i:i+1].lower() for i in range(0, len(txt), 1)]
    txt = [txt[i:i+1] for i in range(0, len(txt), 1)]
    txt = txt[::-1].split(' ')
    txt = txt[::-1].split()
    txt = txt[::-1].split(',')
    return txt
