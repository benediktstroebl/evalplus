
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
    lst = txt.split()
    if len(lst) == 0:
        lst = txt.split(',')
        if len(lst) == 0:
            lst = []
            for i in range(0, len(txt)):
                if ord(txt[i]) % 2 != 0:
                    lst.append(txt[i])
            return len(lst)
        else:
            return lst
    else:
        return lst


