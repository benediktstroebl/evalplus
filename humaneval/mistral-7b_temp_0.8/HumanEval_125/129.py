
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
    if " " in txt:
        txt_list = txt.split()
    elif "," in txt:
        txt_list = txt.split(",")
    else:
        odd_letters = 0
        for i in txt:
            if i == i.lower():
                if (ord(i) % 2 != 0):
                    odd_letters += 1
        txt_list = odd_letters
    return txt_list

