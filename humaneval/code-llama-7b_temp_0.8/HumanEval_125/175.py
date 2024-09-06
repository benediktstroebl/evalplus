
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
    
    # create list of words
    words = [word for word in txt.split()]

    # if no whitespaces in string then split on commas
    if len(words) == 0:
        words = [word for word in txt.split(',')]

    # if still no words, return number of letters with odd order in alphabet
    if len(words) == 0:
        words = sum(ord(char) % 2 for char in txt)

    # return list of words
    return words

