
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
    if ' ' in txt:
        return txt.split()
    else:
        n = len(txt)
        for i in range(n):
            if txt[i] == 'a' or txt[i] == 'b' or txt[i] == 'c' or txt[i] == 'd' or txt[i] == 'e' or txt[i] == 'f':
                if i % 2 == 1:
                    return n
                else:
                    continue
        return 0
