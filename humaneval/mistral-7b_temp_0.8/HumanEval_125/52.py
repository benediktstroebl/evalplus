
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
    import re
    import string

    word_list = []
    if re.search("([a-zA-Z]+)", txt):
        word_list = re.split("([a-zA-Z]+)", txt)
    else:
        for letter in string.ascii_lowercase:
            if ord(letter) % 2 == 0:
                word_list.append(letter)
    return word_list

