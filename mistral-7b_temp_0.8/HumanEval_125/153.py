
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
    # Words = txt.split()
    # return Words
    # if " " not in txt:
    #     return ","
    # elif "," not in txt:
    #     for i in txt:
    #         if i == "a" or "b" or "c" or "d" or "e" or "f" or "g" or "h" or "i" or "j" or "k" or "l" or "m" or "n" or "o" or "p" or "q" or "r" or "s" or "t" or "u" or "v" or "w" or "x" or "y" or "z":
    #             return i
    # elif "," in txt:
    #     Words = txt.split(",")
    #     return Words
    # else:
    #     return "No Characters Found"
    # return True

    # if " " not in txt:
    #     return ","
    # elif "," not in txt:
    #     for i in txt:
    #         if i == "
