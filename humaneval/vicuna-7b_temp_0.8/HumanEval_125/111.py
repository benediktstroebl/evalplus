
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
    # split words in txt by whitespaces
    words = txt.split()
    # if there is no whitespaces, split on commas
    if not words:
        words = txt.split(',')
    # if there is no whitespaces and no commas, return odd number of lower-case letters
    if not words and not txt.count(','):
        words = [i for i in txt.lower() if i.isalpha() and ord(i) % 2 == 1]
    return words
