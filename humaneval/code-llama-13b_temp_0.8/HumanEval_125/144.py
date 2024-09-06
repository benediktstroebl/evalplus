
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
    x = False
    for i in txt:
        if i == ' ' or i == ',':
            x = True
        if x and i != ' ' and i != ',':
            lst.append(i)
    
    if not x:
        return len([i for i in txt if ord(i)%2 == 1 and ord(i) >= ord('a') and ord(i) <= ord('z')])
    return ''.join(lst).split()

