
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
    if not txt:
        return None
    word_list = txt.split()
    word_list_no_spaces = [word.strip() for word in word_list]
    if len(word_list)!= len(word_list_no_spaces):
        word_list = word_list_no_spaces
    return word_list
