
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
    txt = txt.lower() # make lowercase
    txt = txt.split()  # split on whitespace
    if txt:  # check if txt is not empty
        txt = txt[0]  # take the first word
        txt = txt.split(',')  # split on comma
        if txt:  # check if txt is not empty
            return txt  # return the first word
        else:
            # check if txt is a palindrome string
            txt = txt[::-1]
            if txt == txt[:len(txt)]:
                return len(txt) + 1  # if txt is a palindrome
            else:
                return 0  # if txt is not a palindrome
    else:
        return 0  # if txt is empty
