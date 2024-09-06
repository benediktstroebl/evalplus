
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

    
    import string
    
    def split_words_1(txt):
        '''
        Given a string of words, return a list of words split on whitespace, if no whitespaces exists in the text you
        should split on commas ',' if no commas exists you should return the number of lower-case letters with odd order in the
        alphabet, ord('a') = 0, ord('b') = 1,... ord('z') = 25
        Examples
        split_words("Hello world!") ➞ ["Hello", "world!"]
        split_words("Hello,world!") ➞ ["Hello", "world!"]
        split_words("abcdef") == 3 
        '''
        a = 0
        for i in txt:
            if i =='':
                txt = txt.replace(i,',')
        txt = txt.split(',')
        for i in txt:
            if i.islower():
                a += 1
        return a
    
    def split_words_2(txt):
        '''
        Given a string
