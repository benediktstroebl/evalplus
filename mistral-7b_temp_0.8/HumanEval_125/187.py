
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
    import string
    if txt.isalpha():
        return [char for char in txt.lower() if ord(char) < 127]
    words = txt.split(" ")
    if words == []:
        return [ord(char) for char in txt.lower() if ord(char) in string.ascii_lowercase and ord(char) % 2 != 0]
    return words
