
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
    lst = []
    lst1 = []
    if txt.find(" ") == -1 and txt.find(",") == -1:
        lst = [ord(t) for t in txt]
        lst1 = [i for i in lst if i % 2 == 1]
        return len(lst1)
    else:
        if txt.find(" ") != -1:
            lst = txt.split(" ")
            return lst
        else:
            lst = txt.split(",")
            return lst
    
