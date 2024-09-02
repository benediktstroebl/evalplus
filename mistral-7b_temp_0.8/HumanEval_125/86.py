
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
    words_list = []
    if " " in txt:
        words_list = txt.split(" ")
    elif "," in txt:
        words_list = txt.split(",")
    else:
        word_list = []
        for letter in txt:
            if ord(letter) % 2 == 0:
                word_list.append(letter)
        words_list.append(word_list)
    return words_list

