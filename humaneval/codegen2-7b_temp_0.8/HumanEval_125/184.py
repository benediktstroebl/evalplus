
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
    txt = txt.split()
    list_of_words = []
    for i in txt:
        if len(i.split("-")) > 1:
            list_of_words.append(i.split("-"))
        else:
            list_of_words.append(i.split(","))
            list_of_words.append(i.split(";"))
    
    return list_of_
