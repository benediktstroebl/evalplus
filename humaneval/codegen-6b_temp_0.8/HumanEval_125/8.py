
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
    txt=txt.split(" ")
    split_words=[]
    letters=0
    for i in txt:
        if i.isalpha() and i.isupper():
            letters+=1
        elif i.isalpha() and i.islower():
            if ord(i[0])%2==1:
                letters+=1
        elif i.isalpha() and i.isdigit():
            letters+=1
        elif i.isalpha() and i.isnumeric():
            letters+=1
        elif i.isspace():
            letters+=1
        elif i.isdigit():
            letters+=1
        elif i.isnumeric():
            letters+=1
        elif i.isspace():
            letters+=1

    if letters%2==1:
        return True
    else:
        return False
