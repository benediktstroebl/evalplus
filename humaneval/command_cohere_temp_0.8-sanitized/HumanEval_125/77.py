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
    # split the string on whitespace or comma if they exist
    # use regrex to match comma since regex ',' is a literal comma and won't work
    if re.search(r'\s|,', txt):
        return txt.split(maxsplit=1)
    # if comma and whitespace don't exist, check for lowercase letters only
    elif 'a' <= txt <= 'z':
        return len(txt) if sum(1 for _ in txt if _.islower()) % 2 == 1 else 3
    else:
        return 1 if txt.lower() == txt else 2