
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
    list_words = txt.split()
    if len(list_words) == 0:
        new_list = []
        for i in range(ord('a'), ord('z') + 1):
            if i % 2 == 1:
                new_list.append(chr(i))
        return len(new_list)
    elif len(list_words) == 1:
        return len(list_words)
    else:
        return list_words

