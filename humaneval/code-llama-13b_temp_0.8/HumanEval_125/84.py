
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
    # 1) Separate words with whitespaces
    # 2) Separate words with commas
    # 3) Odd letters
    
    for x in txt:
        if x == ' ':
            return txt.split()
        elif x == ',':
            return txt.split(',')
        elif x.islower:
            ord_alp = 0
            for i in txt:
                if i.islower():
                    ord_alp += ord(i)
            if ord_alp % 2 != 0:
                return ord_alp // 2
                
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
