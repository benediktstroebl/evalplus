
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
    if not txt:
        return []
    result = []
    for word in txt.split():
        if len(word) == 1 or ',' in word:
            result.append(word)
        else:
            if word.islower():
                result.append(word)
            elif word.isupper():
                result.append(word)
            else:
                result.append(word.lower())
                result.append(word.upper())
    return result
