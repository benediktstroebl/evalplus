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
    no_space = re.compile("\s")
    no_comma = re.compile(",")
    if no_space.search(txt) and no_comma.search(txt):
        return ["Should Split on whitespace or commas"]
    elif no_space.search(txt):
        return re.split(r"\s+", txt)
    elif no_comma.search(txt):
        return re.split(r",+", txt)
    else:
        return len(list(re.findall(r'([a-z][01]?\d?){4}', txt)))