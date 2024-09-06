
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

    words = txt.split()
    if len(words) == 0:
        words = txt.split(",")
        if len(words) == 0:
            res = list(set(chr(c) for c in range(ord('a'),ord('z')+1) if ord(c) % 2 == 1))
            return len(res)
        else:
            return words
    else:
        return words


