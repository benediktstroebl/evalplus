
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
    a=[]
    b=[]
    c=0
    d=0
    e=0
    for i in txt:
        if i.isalpha():
            a.append(i)
        elif i.isspace():
            b.append(a)
            a=[]
            continue
        else:
            b.append(a)
            a=[]
            continue

    for i in b:
        for j in i:
            if j.islower() and ord(j) % 2 != 0:
                d+=1
    return b


