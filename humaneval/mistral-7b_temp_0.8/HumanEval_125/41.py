
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

    #split_words("Hello,world!") ➞ ["Hello", "world!"]
    #split_words("abcdef") == 3

    #return txt.split()
    if len(txt) == 0:
        return []
    elif len(txt) == 1:
        return txt
    else:
        if txt[0] == ' ':
            return []
        elif txt[-1] == ' ':
            return []
        else:
            if txt[0].isalpha():
                return [txt[0]]
            elif txt[-1].isalpha():
                return [txt[-1]]
            else:
                return []































































































