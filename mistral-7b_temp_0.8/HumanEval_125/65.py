
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
    res = []
    count = 0
    txt = txt.lower()
    for i in range(0, len(txt)):
        if txt[i] in [" ","\n", "\t", "\r"]:
            if count > 0:
                res.append(txt[i - count : i])
                count = 0
            else:
                res.append("")
        else:
            if ord(txt[i]) % 2 == 1:
                count += 1
    if count > 0:
        res.append(txt[i - count : i + 1])
    return res

