
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
    #  Split on whitespace:
    splitted_words = txt.split()
    #  Split on comma:
    if not splitted_words:
        splitted_words = txt.split(",")
    #  Return number of lowercase letters with odd order in the alphabet:
    if not splitted_words:
        for letter in txt.lower():
            if (ord(letter) - ord("a")) % 2 == 1:
                return 1
        return 0

    #  Return the list of words:
    return splitted_words

