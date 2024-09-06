
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
    lst = []
    if txt.isalpha():
        for i in range(len(txt)):
            if ord(txt[i])%2 != 0:
                lst.append(txt[i])
        return lst
    elif txt.isalnum():
        lst = txt.split()
    else:
        return len([char for char in txt if char.islower()])
    return lst
