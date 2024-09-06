
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
    if not txt:
        return 0
    if txt.find(' ') == -1:
        if txt.find(',') == -1:
            return split_words(''.join(ch for i, ch in enumerate(txt) if (i + 1) % 2 != 0))
        else:
            return split_words(txt.replace(',', ' '))
    else:
        return txt.split(' ')
