
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
    txt = txt.lower()
    split_list = txt.split()
    split_words = []
    for i in split_list:
        if i == '':
            split_list.remove(i)
            split_list.append(i)
        else:
            split_words.append(i)
    if len(split_list) == 0:
        split_list.append('')
    return split_list
