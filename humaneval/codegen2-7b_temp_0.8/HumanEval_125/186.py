
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
    
    s=txt.split(" ")
    s_lower=[]
    for i in s:
        if i.isalpha():
            s_lower.append(i.lower())
    if len(s_lower)==0:
        s_lower=txt.split(',')
    if len(s_lower)==0:
        s_lower=txt.split('')
    return s_lower
    
    

    
    
    
    
    
    
    
    
    
    
    
    
