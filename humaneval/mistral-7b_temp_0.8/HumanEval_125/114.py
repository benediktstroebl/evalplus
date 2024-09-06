
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
    if words == []:
        for x in txt:
            if x == 'a':
                a += 1
            elif x == 'e':
                e += 1
            elif x == 'i':
                i += 1
            elif x == 'o':
                o += 1
            elif x == 'u':
                u += 1
            else:
                n += 1
        return a + e + i + o + u + n
    return words


