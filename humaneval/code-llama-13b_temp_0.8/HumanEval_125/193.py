
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
    if len(txt.split())>0:
        return txt.split()
    if len(txt.split(','))>0:
        return txt.split(',')
    txt=txt.lower()
    count=0
    for letter in txt:
        if ord(letter)>=96 and ord(letter)<=122:
            if (ord(letter)-96)%2!=0:
                count+=1
    return count

    
    
