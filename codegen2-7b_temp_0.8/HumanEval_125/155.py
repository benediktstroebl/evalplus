
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
    if len(txt) == 0:
        return []
    words = []
    for word in txt.split():
        if len(word) == 0:
            continue
        if word[0] == ',':
            words.extend([',']*len(word[1:].split()))
        else:
            words.extend([word[i].lower() for i in range(len(word)) if word[i].isalpha() and ord(word[i])%2!= 0])
    return
