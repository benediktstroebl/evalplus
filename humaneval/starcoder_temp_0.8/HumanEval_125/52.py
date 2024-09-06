
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
    def Split_on_Commas(txt):
        '''
        Given a string of words, return a list of words split on commas, if no commas exists you should return the number of lower-case letters with odd order in the alphabet, ord('a') = 0, ord('b') = 1,... ord('z') = 25
        Examples
        split_words("Hello world!") ➞ ["Hello", "world!"]
        split_words("Hello,world!") ➞ ["Hello", "world!"]
        split_words("abcdef") == 3 
        '''
        txt = txt.split(",")
        return txt

    def Split_on_Whitespace(txt):
        '''
        Given a string of words, return a list of words split on whitespace, if no whitespaces exists in the text you
        should split on commas ',' if no commas exists you should return the number of lower-case letters with odd order in the
        alphabet, ord('a') = 0, ord('b') = 1,... ord('z') = 25
        Examples
        split_words("Hello world!") ➞ ["Hello", "world!"]
        split_words("Hello,world!") ➞ ["Hello", "world!"]
        split_words("abcdef") == 3 
        '''
        txt = txt.split(" ")
        return txt

    def count_odd_lower(txt):
        '''
        Given a string of words, return a list of words split on whitespace, if no whitespaces exists in the text you
        should split on commas ',' if no commas exists you should return the number of lower-case letters with odd order in the
        alphabet, ord('a') = 0, ord('b') = 1,... ord('z') = 25
        Examples
        split_words("Hello world!") ➞ ["Hello", "world!"]
        split_words("Hello,world!") ➞ ["Hello", "world!"]
        split_words("abcdef") == 3 
        '''
        count = 0
        for i in txt:
            if i.islower() == True:
                if ord(i)%2!= 0:
                    count = count + 1
        return count

    # Try Splitting on Commas and Splitting on Whitespace
    try:
        return Split_on_Whitespace(txt)
    except:
        return Split_on_Commas(txt)

    #
