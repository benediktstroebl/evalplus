
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

    # Split string on whitespace
    words = txt.split()
    if not words:
        return []

    # Split string on comma
    if len(words) == 1:
        return [words[0].split(",")]

    # Split string on lower-case letters with odd order in the alphabet
    if len(words) == 1:
        words = [x for x in words[0] if ord(x) % 2 != 0]

    return words

