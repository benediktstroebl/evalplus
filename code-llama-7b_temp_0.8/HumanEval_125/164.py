
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

    # PLAN
    # if txt contains spaces, split by spaces
    # if txt contains no spaces, split by commas
    # if txt contains no spaces or commas, return the number of lower-case letters with odd order in the alphabet
    
    # check for spaces
    if " " in txt:
        return txt.split(" ")

    # check for commas
    if "," in txt:
        return txt.split(",")

    # check for spaces and commas
    if " " not in txt and "," not in txt:
        odd_letters = 0
        for i in range(1, len(txt) + 1):
            if ord(txt[i - 1]) % 2 == 1:
                odd_letters += 1
        return odd_letters



    return split_words(txt)

