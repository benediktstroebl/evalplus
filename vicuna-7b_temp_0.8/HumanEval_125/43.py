
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
    txt = txt.replace(" ", "")
    txt = txt.replace(",", "")
    txt = txt.split()
    txt = txt[::2] + [txt[1] + txt[0]]
    txt = [ord(txt[i]) for i in range(len(txt))]
    txt = [i for i in txt if i > 0]
    txt = [i for i in txt if (i + 1) % 2 == 0]
    return txt
