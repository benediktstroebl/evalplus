
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
    words = txt.split()
    if txt.count(' ') == 0:
        return words
    words = [word.lower() for word in words]
    if txt.count(',') == 0:
        return words
    odd_words = [word for word in words if word[0].islower() and ord(word[0]) % 2!= 0]
    even_words = [word for word in words if word[0].islower() and ord(word[0]) % 2 == 0]
    return odd_words + even_words
