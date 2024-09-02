
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
    splitter = "abcdefghijklmnopqrstuvwxyz"
    words = []
    for letter in txt:
        if letter in splitter:
            if splitter.index(letter) % 2 == 1:
                words.append(letter)
            else:
                words.remove(letter)
    return words
