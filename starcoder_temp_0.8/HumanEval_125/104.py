
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

    if txt.find(' ')!= -1:
        return txt.split(' ')
    elif txt.find(',')!= -1:
        return txt.split(',')
    else:
        i = 1
        word_list = []
        for x in txt:
            if i % 2!= 0:
                word_list.append(x)
            i += 1
        return len(word_list)

