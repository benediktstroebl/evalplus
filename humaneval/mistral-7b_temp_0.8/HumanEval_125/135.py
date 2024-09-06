
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
    # Write your code here
    if " " in txt or "," in txt:
        return txt.split(" ")
    else:
        txt_lst = []
        for i in txt:
            if i.lower() not in txt_lst:
                txt_lst.append(i.lower())
        return len(txt_lst)
