
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
    #txt = str(txt)
    if (type(txt) == str and len(txt) > 0):
        letters = 0
        for x in txt:
            if ord(x) == 32 or ord(x) == 45 or ord(x) == 46:
                continue
            else:
                letters += 1
        # txt = txt.split(' ')
        # return txt
        # if len(txt) == 1:
        #     return len(''.join(txt))
        # else:
        #     return len(txt[len(txt) -1])
        return letters
    else:
        return 0
