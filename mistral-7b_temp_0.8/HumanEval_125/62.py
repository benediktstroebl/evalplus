
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
    list_words=[]
    #if txt.find(" "):
    #    list_words=txt.split(" ")
    #elif txt.find(","):
    #    list_words=txt.split(",")
    #else:
    #    list_words=[ord(i)-ord("a") for i in txt]
    #return list_words
    for i in range(len(txt)):
        if txt[i] == " " or txt[i] == ",":
            txt = txt[i+1:]
            break
    if txt.find(" "):
        list_words=txt.split(" ")
    elif txt.find(","):
        list_words=txt.split(",")
    else:
        list_words=[ord(i)-ord("a") for i in txt]
    return list_words

