
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
    
    def helper(txt,word_list):
        if len(txt)==0:
            return word_list
        if len(txt)>0 and txt[-1].isalpha():
            word_list.append(txt)
            return helper(txt[:-1],word_list)
        if len(txt)>0 and not txt[-1].isalpha():
            return helper(txt[:-1],word_list)
    
    return helper(txt,[])
