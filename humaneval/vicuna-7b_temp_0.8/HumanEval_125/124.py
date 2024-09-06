
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
    txt = txt.lower() # convert text to lowercase
    words = txt.split()  # split on whitespace
    if len(words) == 1 and words[0].endswith('.') or len(words) == 2 and words[0] == '.' and words[1].isalpha() or len(words) == 0: # split on commas
        words = txt.split(',')
    if ' ' in txt:  # split on whitespaces
        words = txt.split()
    if len(words) > 25:  # split on uppercase letters
        words = txt.split()
    return words
