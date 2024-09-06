
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
    if len(txt) == 0:
        return 0
    lst=[]
    if ' ' in txt:
        lst=txt.split(' ')
        return lst
    elif ', ' in txt:
        lst=txt.split(', ')
        return lst
    else:
        odd_lst=[]
        for i in range(len(txt)):
            if ord(txt[i])%2==1:
                odd_lst.append(txt[i])
        return odd_lst
    
    
