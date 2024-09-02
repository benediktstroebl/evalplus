
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
    if not isinstance(txt, str):
        return None
    if ' ' in txt:
        return txt.split(' ')
    if ',' in txt:
        return txt.split(',')
    else:
        l = 0
        for i in txt:
            if j == ord('a') or j == ord('b') or j == ord('c') or j == ord('d') or j == ord('e') or j == ord('f') or j == ord('g') or j == ord('h') or j == ord('i') or j == ord('j') or j == ord('k') or j == ord('l') or j == ord('m') or j == ord('n') or j == ord('o') or j == ord('p') or j == ord('q') or j == ord('r') or j == ord('s') or j == ord('t') or j == ord('u') or j == ord('v') or j == ord('w') or j == ord('x') or j == ord('y') or j == ord('z'):
                l += 1
        return l

