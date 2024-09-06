
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
    #my solution
    if txt.count(' ') == 0 and txt.count(',') == 0:
        return len(list(filter(lambda x: ord(x) % 2 == 1, list(txt))))
    elif txt.count(' ') == 0:
        return txt.count(',')
    elif txt.count(',') == 0:
        return len(list(filter(lambda x: ord(x) % 2 == 1, list(txt))))
    else:
        return txt.split()

    #best solution
    # txt = txt.replace(',',' ')
    # return txt.split()

    # second best solution
    # return list(txt.split(' ')) if ' ' in txt else txt.split(',')

    # third best solution
    # return list(txt.split(' ')) if ' ' in txt else list(txt.split(','))
