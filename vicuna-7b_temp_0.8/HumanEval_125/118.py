
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
    # Handle the case when the txt is None or empty
    if txt is None or txt == '':
        return []
    txt = txt.lower()
    # Split the text on whitespace
    words = txt.split()
    # Split the text on commas if it is not empty
    if ',' in words:
        words = [word for word in words if word not in set(['', ','])]
    # handle the case when the txt is empty
    if not words:
        if len(txt) % 25 == 0:
            return [txt[::25].lower()]
        else:
            return [txt[::26].lower()]
    return words
