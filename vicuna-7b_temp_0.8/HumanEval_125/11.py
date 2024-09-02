
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
    txt = txt.lower()
    if txt.strip() == "":
        return [0]
    txt_list = txt.split()
    txt_list = [txt_list[i:i+2] if i+1 == len(txt_list) else txt_list[i] for i in range(len(txt_list)) if txt_list[i] != ""]
    txt_list = ["".join(txt_list) if txt_list[-1] != "" else "" for txt_list in txt_list]
    return txt_list
