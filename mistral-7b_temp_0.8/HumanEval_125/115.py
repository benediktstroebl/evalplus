
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
    return ['', '']

    # Split on whitespace, if no whitespace exists in the text split on commas
    # If no commas exist return the number of lower-case letters with odd order in the alphabet, ord('a') = 0, ord('b') = 1, ... ord('z') = 25

    # You can return an empty array if there are no words in the text.

    # We should split on the first space we see
