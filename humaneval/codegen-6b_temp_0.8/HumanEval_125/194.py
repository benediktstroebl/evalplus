
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
    import string
    d = {}
    for char in string.ascii_lowercase:
        d[char] = 0

    for word in txt.split():
        for char in word:
            d[char] = d[char] + 1

    odds = 0
    for key, value in d.items():
        if value % 2 != 0:
            odds = odds + 1

    return odds


