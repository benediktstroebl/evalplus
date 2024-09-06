
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
    if ' ' in txt:
        lst = txt.replace(' ', '').split(',')
    elif ',' in txt:
        lst = txt.replace(',', '').split(' ')
    else:
        lst =[txt]
    for i in range(len(lst)):
        lst[i] = lst[i].lower()
        if ord(lst[i][0]) %2:
            lst[i] = ord(lst[i][0])*(len(lst[i])+1)
        else:
            lst[i] = ord(lst[i][-1])*len(lst[i])
    return lst
