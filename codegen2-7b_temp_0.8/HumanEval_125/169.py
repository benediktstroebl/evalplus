
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
    if txt.isspace():
        return [txt]

    words = txt.split(' ')
    for i in range(len(words)):
        words[i] = words[i].lower()
        if words[i].isalpha():
            words[i] = ord(words[i]) % 2
            if words[i] == 1:
                words[i] = ord(words[i]) - 1
                words[i] = chr(words[i])
            else:
                words[i] = chr(words[i])

    return words

