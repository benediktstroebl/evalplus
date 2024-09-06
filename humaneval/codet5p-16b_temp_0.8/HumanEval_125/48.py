
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

    if ',' not in txt and'' not in txt:
        return ord(txt.lower()[1])
    elif ',' not in txt:
        return [word.lower() for word in txt.split() if word[0] == word[0].lower()]
    elif'' not in txt:
        return [word.lower() for word in txt.split(',') if word[0] == word[0].lower()]
    else:
        return [word.lower() for word in txt.split()]
