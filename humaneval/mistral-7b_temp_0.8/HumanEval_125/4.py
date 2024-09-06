
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
    # make a list of split words
    # if there is a whitespace, split on the whitespace
    # if there is no whitespace, split on the commas
    # if there are no commas, split by the length of the odd alphabet letters
    # return the list
    if ' ' in txt:
        return txt.split()
    if ',' in txt:
        return txt.split(',')
    odd_words = ''
    for letter in txt:
        if ord(letter) % 2 == 0:
            pass
        else:
            odd_words += letter
    return odd_words
