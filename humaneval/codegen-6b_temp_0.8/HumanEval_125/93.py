
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
    #split string into list of words delimited by space
    txt_list = txt.split(' ')

    #loop through list of words and remove any empty elements, will remove comma but keep space
    for txt in txt_list:
        if not txt:
            txt_list.remove(txt)
    return txt_list


