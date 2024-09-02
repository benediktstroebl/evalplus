
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
        lst = txt.split(" ")
    elif "," in txt:
        lst = txt.split(",")
    else:
        cnt = 0
        for x in range(0, len(txt)):
            y = ord(txt[x]) - ord('a')
            if y % 2 == 1:
                cnt += 1
        return cnt
    return lst
