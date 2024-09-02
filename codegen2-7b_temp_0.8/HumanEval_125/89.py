
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
    txt_list = txt.split()
    if not txt_list:
        return txt_list
    new_list = []
    for i in range(len(txt_list)):
        if not txt_list[i].isalpha():
            new_list.append(txt_list[i])
            continue
        if txt_list[i].isalpha():
            new_list.append(txt_list[i])
        else:
            new_list.append(txt_list[i].lower())
    return new_
