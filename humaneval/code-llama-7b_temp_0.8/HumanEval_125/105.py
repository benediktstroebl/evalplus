
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
    
    #check for whitespace
    #split on whitespace
    #if not whitespace then check for commas and split on commas
    #if no whitespace and no commas then return the number of lower-case letters with odd order in the alphabet
    #if whitespace then return list of string split on whitespace
    #if no commas return list of string split on whitespace
    
    if (txt.find(" ") == -1) and (txt.find(",") == -1):
        #no whitespace or commas
        odd = []
        for i in range(0,26):
            if (i%2) != 0:
                odd.append(chr(i+ord('a')))
        return len(odd)
    elif txt.find(" ") == -1:
        #no whitespace
        return txt.split(",")
    else:
        #there is whitespace
        return txt.split(" ")
    
    
    
    
    
    
    
