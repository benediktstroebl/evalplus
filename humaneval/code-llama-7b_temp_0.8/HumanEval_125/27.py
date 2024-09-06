
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
    # print(ord("a"), ord("b"), ord("c"), ord("d"), ord("e"), ord("f"))
    # if not txt.find(" "):
    #     return 
    if not txt.find(","):
        return 
    else:
        return [w.strip() for w in txt.split(",")]

