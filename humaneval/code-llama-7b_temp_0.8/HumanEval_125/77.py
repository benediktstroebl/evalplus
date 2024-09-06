
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
    def odd_words(txt):
        if len(txt) < 1:
            return 0
        i = ord(txt[0])
        if i % 2 == 0:
            return odd_words(txt[1:])
        else:
            return 1 + odd_words(txt[1:])
    if len(txt) == 0:
        return []
    else:
        if len(re.split('[ ,]', txt)) == 1:
            return [str(odd_words(txt))]
        else:
            return re.split('[ ,]', txt)


