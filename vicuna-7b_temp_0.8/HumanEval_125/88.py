
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
    txt = txt.split()
    if txt:
        return txt
    else:
        a = [ord(c) for c in "abcdefghijklmnopqrstuvwxyz"]
        for i in range(len(a)):
            if a[i] % 2 == 1:
                txt = txt + [a[i]]
                return txt
        return 26
