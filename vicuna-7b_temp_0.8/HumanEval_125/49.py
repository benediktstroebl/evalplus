
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
    txt = txt.lower()
    if txt:
        words = txt.split()
        if not words:
            words = txt.split(',')
        return words
    else:
        string_chars = set(range(ord('a'), ord('z') + 1))
        odd_chars = [c for c in string_chars if c % 2 == 1]
        return [c for c in txt if c in odd_chars]