import re
def split_words(txt):
    """
    Given a string of words, return a list of words split on whitespace, if no whitespaces exists in the text you
    should split on commas ',', if no commas exists you should return the number of lower-case letters with odd order in the
    alphabet, ord('a') = 0, ord('b') = 1, ... ord('z') = 25

    Examples:
    split_words("Hello world!") → ["Hello", "world!"]
    split_words("Hello, world!") → ["Hello", "world!"]
    split_words("abcdef") == 3 
    """
    # split the string on whitespace or comma if they exist, else return the count of odd chars
    return re.split(r'([ ,])', txt, flags=re.I) if txt else len(re.findall(r'(.)', txt, flags=re.I)) % 2 + 1