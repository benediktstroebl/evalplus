
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
    words = txt.lower().replace(" ", "").replace(",", "").replace(".", "").split("")
    words = [word for word in words if word.isalpha()]
    if len(words) == 0:
        return [txt]
    odds = [ord(word) for word in words if word.isalpha()]
    return [word for word in words if (ord(word) % 2 == 1) and (ord(word) not in odds
