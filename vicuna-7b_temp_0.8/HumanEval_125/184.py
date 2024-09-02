
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
    # Check if text is only a number or contains only digits
    if re.search(r'\d+', txt):
        return [txt]

    # Check if text is empty
    if not txt:
        return []

    # Check if text is a single word
    if txt.isalpha():
        # Split on whitespace
        words = txt.split()
        # If text is not empty and only contains one word, return that word
        if len(words) == 1 and txt != '':
            return [words[0]]
        # Otherwise return a list of words
        return words

    # Check if text is a punctuation
    if re.search(r'\W', txt):
        return txt.split()

    # Check if text is a string with a single quote
    if re.search(r"'", txt):
        txt = txt.replace("'", "")
        return [txt]

    # Split on whitespace or comma
    words = txt.split()

    if not words:
        # If there are no spaces or commas in the text, it's empty
        return []
    else:
        # If there are spaces or commas in the text, split on them
        return words
