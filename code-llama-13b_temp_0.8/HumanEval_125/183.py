
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
    try:
        txt.index(' ')
        return txt.split(' ')
    except ValueError:
        try:
            txt.index(',')
            return txt.split(',')
        except ValueError:
            count=0
            for i in txt:
                if i.islower():
                    count += ord(i)-96
                    if count%2==1:
                        return count
