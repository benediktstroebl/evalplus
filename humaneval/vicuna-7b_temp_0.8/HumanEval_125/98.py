
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

    # split on whitespace
    if txt == "":
        return [txt]

    # split on commas
    words = txt.split(',')

    # convert to lowercase
    words = [word.lower() for word in words]

    # count the number of lower-case letters with odd order in the alphabet
    letters = 'abcdefghijklmnopqrstuvwxyz'
    odd_letters = 0
    for letter in letters:
        if letter.islower():
            if letter - 'a' % 2 == 1:
                odd_letters += 1

    # return the words
    return words
