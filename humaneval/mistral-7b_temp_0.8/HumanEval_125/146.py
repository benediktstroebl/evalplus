
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

    splitted_words = []
    if ' ' in txt:
        splitted_words = txt.split(" ")
        return splitted_words
    elif ',' in txt:
        splitted_words = txt.split(",")
        return splitted_words
    else:
        splitted_words = list(txt)
        word = ""
        for i in splitted_words:
            if ord(i) % 2 == 0:
                word += i
        return word
