
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
    # check for whitespaces and split the text
    if " " in txt:
        txt = txt.split(" ")
    elif ":" in txt:
        txt = txt.split(":")
    elif ", " in txt:
        txt = txt.split(", ")
    elif "." in txt:
        txt = txt.split(".")
    else:
        # split on all alphabets
        txt = txt.split("")
        # sort the txt
        txt = sorted(txt)
        # check for odd order of letters
        odd = 0
        for i in range(len(txt)):
            if txt[i] >= ord("a"):
                odd += 1
        return odd
