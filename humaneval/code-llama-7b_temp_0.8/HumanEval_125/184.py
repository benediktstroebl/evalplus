
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

    # split the text on whitespace
    words = txt.split()
    
    # if the result is not an empty list return the list
    if words:
        return words
    
    # split on comma
    words = txt.split(',')
    
    # if the result is not an empty list return the list
    if words:
        return words
    
    # count letters with odd order in the alphabet
    odd_letters = 0
    for letter in txt:
        if (ord(letter) - ord('a')) % 2 == 1:
            odd_letters += 1
            
    return odd_letters
    
    
