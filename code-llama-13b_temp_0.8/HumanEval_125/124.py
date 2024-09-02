
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
    if len(txt)==0:
        return []
    elif len(txt.split())>0:
        return txt.split()
    else:
        count=0
        for i in range(len(txt)):
            if i%2==0 and ord(txt[i])<=ord('z'):
                count+=1
        return count
    
    
