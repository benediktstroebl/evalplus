
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
    # replace whitespaces with a single whitespace
    txt = txt.replace(" ", " ")
    # replace commas with a single comma
    txt = txt.replace(",", ",")
    # remove extra commas
    txt = txt.replace(",","")
    # find lower-case letters with odd order in the alphabet
    txt = txt.lower()
    txt = txt.split("")
    txt = [ord(ch) for ch in txt]
    txt = [x for x in txt if x > 0 and x % 2 == 1]
    # replace whitespaces
    txt = txt.join(" ")
    return txt
