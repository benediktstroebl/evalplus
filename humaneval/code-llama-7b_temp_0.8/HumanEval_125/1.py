
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
    if txt.find(" ") == -1 and txt.find(",") == -1:
        a = 0
        for i in range(len(txt)):
            if ord(txt[i])%2==1:
                a+=1
        return a
    if txt.find(" ") == -1:
        return txt.split(",")
    if txt.find(",") == -1:
        return txt.split(" ")
    else:
        return txt.split(" ")
    
