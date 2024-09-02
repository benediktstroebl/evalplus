
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
    if not txt:
        return []
    elif not any(txt.isalpha()):
        return [0]
    elif not any(txt.isalnum()):
        return [txt]
    else:
        lst = []
        lst2 = []
        for i in txt:
            if i.isalpha():
                lst.append(i)
            elif i.isalpha() and not lst[-1].isalpha():
                lst2.append(''.join(lst))
                lst = []
        if lst:
            lst2.append(''.join(lst))
        return lst2


