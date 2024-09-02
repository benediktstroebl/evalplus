
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
    # if there is a whitespace split on whitespace
    if txt.isspace() == False:
        return txt.split()
    # if there is not whitespace split on commas
    elif txt.find(',') != -1:
        return txt.split(',')
    # if there is not whitespace split or commas return the number of lower-case letters with odd order in the alphabet, ord('a') = 0, ord('b') = 1, ... ord('z') = 25
    else:
        word = ''
        lower_case = 0
        for i in txt:
            if i.isupper() == False:
                word += i
            else:
                lower_case += 1
        return lower_case
