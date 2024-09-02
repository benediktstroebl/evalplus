
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
    # handle empty string
    if not txt:
        return []

    txt = txt.strip()
    # handle single space
    if txt == " ":
        return [txt]

    txt = txt.lower()
    txt_list = txt.split()
    txt_list = [txt_list[i:i+2] if i+1 in txt_list else txt_list[i] for i in range(0, len(txt_list), 2)]
    txt_list = [txt_list[j::2] for j in txt_list]
    txt_list = [" ".join(txt_list) for txt_list in txt_list]
    return txt_list