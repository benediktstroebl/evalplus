
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
    txt = txt.lower() # make the text lowercase so that ord() works
    words = txt.split() # split the text into a list of words
    if len(words) > 0:
        return words
    else:
        # if no spaces exist, split on commas
        commas = txt.split(',')
        if len(commas) > 0:
            return commas
        else:
            # if no commas exist, count the number of lower-case letters with odd order in the alphabet
            alphabet = 'abcdefghijklmnopqrstuvwxyz'
            count = 0
            for letter in txt:
                count += ord(letter) % 2
            return count
