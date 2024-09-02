
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
    if len(txt) == 0:
        return 0
    elif len(txt.split()) > 0:
        return txt.split()
    elif len(txt.split(',')) > 0:
        return txt.split(',')
    else:
        count = 0
        for i in range(len(txt)):
            if ord(txt[i]) % 2 != 0 and ord(txt[i]) > 96 and ord(txt[i]) < 123:
                count += 1
        return count
    
    
