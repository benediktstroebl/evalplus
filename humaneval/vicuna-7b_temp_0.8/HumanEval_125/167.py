
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
    words = txt.split()
    if not words:
        num = sum(ord(c) for c in txt) % 26
        if num == 0:
            return [txt]
        else:
            return [txt[i:i+ord(c)] for c in txt if ord(c) > ord('a') and ord(c) < ord('z')]
    else:
        return words
