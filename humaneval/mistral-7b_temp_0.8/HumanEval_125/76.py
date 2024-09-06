
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
    print(words)

    if len(words) == 0:
        a = txt.split(",")
        print(a)
        return a
    elif len(txt) == 1:
        a = ord(txt)
        print(a)
        return a
    else:
        c = 0
        for i in txt:
            if ord(i) % 2 != 0:
                c += 1

        return c

