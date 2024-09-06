
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
    if txt == "":
        return " "
    
    if txt.isspace():
        return txt.split()
    
    if ' ' in txt:
        return txt.split()
    else:
        odd_num = 0
        for letter in txt:
            if ord(letter)%2==1:
                odd_num +=1
        return odd_num
