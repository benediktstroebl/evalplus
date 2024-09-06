
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
    if not txt.isspace():
        txt_list = txt.split()
        return txt_list
    if "," in txt:
        txt_list = txt.split(",")
        return txt_list
    else:
        txt_list = []
        for i in txt:
            if ord(i) % 2 == 1:
                txt_list.append(i)
        return txt_list


