
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
    txt = txt.lower()
    txt = txt.split()
    txt = txt[::2]  # alternate between every other character
    txt = txt.join('')  # join back into a string
    txt = txt.split(',')  # split on commas
    txt = txt.split(' ')  # split on whitespaces
    txt = txt.split()  # split on whitespaces
    txt = txt[::2]  # alternate between every other character
    txt = txt.join('')  # join back into a string
    txt = txt.split(',')  # split on commas
    txt = txt.split(' ')  # split on whitespaces
    if txt.count(' ') == 0 and txt.count(',') == 0:
        txt = ''.join([i for i in txt if i.isalpha() and len(i) % 2 == 1])
    else:
        txt = txt.split(' ')
    return txt
