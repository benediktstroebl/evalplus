
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
    list_1=txt.split()
    if len(list_1) > 0:
        return list_1
    else:
        list_2=txt.split(',')
        if len(list_2) > 0:
            return list_2
        else:
            return sum([1 for char in txt if char.isalpha() and ord(char) % 2 != 0])


    
    
