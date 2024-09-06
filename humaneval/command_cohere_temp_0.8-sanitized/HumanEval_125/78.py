import re
def split_words(txt):
    """
    Given a string of words, return a list of words split on whitespace, if no whitespaces exists in the text you
    should split on commas ',', if no commas exists you should return the number of lower-case letters with odd order in the
    alphabet, ord('a') = 0, ord('b') = 1, ... ord('z') = 25
    Examples
    split_words("Hello world!") → ["Hello", "world!"]
    split_words("Hello, world!") → ["Hello", "world!"]
    split_words("abcdef") == 3 
    """
    no_comma = re.findall(r'\w+', txt)
    if len(no_comma) > 0:
        return re.split(r'\s|,', txt)
    elif ',' in txt:
        return re.split(r',', txt)
    else:
        return len(re.findall(r'\b(\w)*(\w)\1\b', txt))