
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

    # using a variable to store the split words, if the words contains a whitespace then use a split, if it does not then
    # use an ord to find the odd ones.

    words = txt.split()
    if len(words) > 0:
        words = txt.split()
    else:
        words = [ord(letter) for letter in txt if letter.islower()]
    return words


