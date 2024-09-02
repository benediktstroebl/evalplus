
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
    txt = txt.strip()
    if txt:
        txt = txt.lower()
        if txt:
            words = txt.split()
            if words:
                return words
            else:
                txt = txt.replace(",", " ")
                if txt:
                    return txt.split()
                else:
                    if "abcdefghijklmnopqrstuvwxyz" in [c for c in txt]:
                        return 26
                    else:
                        return 0
    else:
        return None
