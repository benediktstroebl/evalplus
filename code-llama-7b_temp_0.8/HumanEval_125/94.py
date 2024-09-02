
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
    count = 0
    for c in txt:
        if ord(c)>=ord('a') and ord(c)<=ord('z'):
            if ord(c)%2==1:
                count+=1
        if c == ' ':
            lst.append(''.join(txt))
            txt = ''
    if count == 0:
        return count
    else:
        return lst

