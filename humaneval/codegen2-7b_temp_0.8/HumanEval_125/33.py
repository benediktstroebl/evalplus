
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
    word_list = txt.split()
    
    if not word_list:
        return []
    
    if word_list[0].isalpha():
        word_list = ['%s%s'%(word_list[0][0], word_list[0][1:]) for word_list in word_list]
        
    else:
        word_list = ['%s%s'%(word_list[0], word_list[1]) for word_list in word_list]
        
    return word_list


