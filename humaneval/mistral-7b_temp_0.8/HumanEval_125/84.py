
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

    words_list = txt.split(' ')
    if len(words_list) == 1:
        words_list = txt.split(',')
    if len(words_list) == 0:
        words_list = len([letter for letter in txt if letter.islower() and ord(letter) % 2 != 0])
    return words_list


