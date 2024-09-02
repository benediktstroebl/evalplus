
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
    # Your code here
    lst = txt.split(' ')
    if len(lst) == 1:
        if ',' in txt:
            lst = txt.split(',')
        else:
            count = 0
            for i in txt:
                if (ord(i) % 2!= 0) and (ord(i) < 122):
                    count += 1
            lst = count
    return lst

