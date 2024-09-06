
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
    if txt == "":
        return None
    else:
        list_words = txt.split(" ")
        if len(list_words) == 0:
            if txt[0].isupper() and txt[-1].isupper():
                return ord("z") - ord("a")
            else:
                return ord(txt[-1]) - ord(txt[0])
        elif len(list_words) == 1:
            if list_words[0][0].isupper():
                return len(list_words[0])
            else:
                return list_words[0][0]
        else:
            return list_words




































































































