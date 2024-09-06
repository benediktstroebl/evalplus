
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
    txt_split = txt.split(" ")
    if txt_split.count("") == 0:
        txt_split = txt.split(",")
    if txt_split.count("") == 0:
        txt_split = len([i for i in txt if i.islower() and chr(ord(i) + 1) != i])
    return txt_split
