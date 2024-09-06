import re
def split_words(txt):
    """
    Given a string of words, return a list of words split on whitespace, if no whitespaces exists in the text you
    should split on commas ',', if no commas exists you should return the number of lower-case letters with odd order in the
    alphabet, ord('a') = 0, ord('b') = 1, ... ord('z') = 25

    Examples:
    split_words("Hello world!") → ["Hello", "world!"]
    split_words("Hello, world!") → ["Hello", "world!"]
    split_words("abcdef") → [3]
    """
    # use regex to split on whitespace or comma
    parts = re.split(r'([ ,])', txt)
    if len(parts) > 1:
        return parts
    # if no commas or whitespace, return number of lowercase letters with odd alphabet order
    # ignoring underscores
    txt = re.sub(r'_[^a-z]', '', txt).lower()
    return [len(re.findall(r'([a-z])', txt)) % 2]