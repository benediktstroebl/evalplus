
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
    ws = txt.split(' ')
    if len(ws) == 0:
        if txt.split(',') == 0:
            c = []
            for i in txt:
                if i.islower():
                    if ord(i) % 2 != 0:
                        c.append(i)
            return len(c)
        else:
            return len(txt.split(','))
    else:
        return len(txt.split(' '))

