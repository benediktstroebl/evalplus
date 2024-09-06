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
    # split on whitespace and commas
    if re.search(r'\s|\,', txt):
        return txt.split(maxsplit=1)
    # If no whitespace or commas, count odd indexed letters
    elif txt.islower():
        return len(list(filter(lambda x: ord(x) % 2, txt)))
    else: 
        return 0