
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

    # split words on whitespace
    words = txt.split()

    # split on comma if no whitespace
    if not words:
        words = txt.split(',')

    # split on letter if no whitespace or comma
    if not words and txt.lower():
        words = txt.split('')

    return words
