
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
    list1=[]
    list2=[]
    list3=[]
    list4=[]
    #str=txt.strip()
    if ' ' in txt:
        list2 = txt.split(' ')
    elif ',' in txt:
        list3 = txt.split(',')
    else:
        x = len(txt)
        for i in range(x):
            if ord(txt[i]) >= ord('a') and ord(txt[i]) <= ord('z'):
                list4.append(txt[i])
        list5 = [i for i in list4 if ord(i) % 2 == 1]
        list6 = len(list5)
        return list6
    list1=list2+list3
    return list1
