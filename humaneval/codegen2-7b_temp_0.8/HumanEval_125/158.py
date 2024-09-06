
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
    txt = txt.lower()
    words = txt.split()
    
    if len(txt) == 0:
        return []
    
    odd = 0
    for i in words:
        if ord(i) % 2!= 0:
            odd += 1
    
    if odd == 0:
        words = [i for i in words if i!= '']
        return words
    
    return [i for i in words if i!= ''
