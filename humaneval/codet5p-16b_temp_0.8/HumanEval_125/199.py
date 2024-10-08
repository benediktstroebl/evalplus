
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

    result = []
    for word in txt.split():
        if word.count(",") == 0 and word.count(" ") == 0:
            result.append(ord(word[0].lower()) * (1 - 2 * (ord(word[0].lower()) % 2)))
        else:
            result.append(word.lower())
    return result
