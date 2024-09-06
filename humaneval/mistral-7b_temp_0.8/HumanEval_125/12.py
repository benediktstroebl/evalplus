
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
    new = txt.split()
    if len(new)==1:
        new = txt.split(',')
        if len(new)==1:
            new = [len(txt) - txt.count('a') - txt.count('b') - txt.count('c') - txt.count('d') - txt.count('e') - txt.count('f') - txt.count('g') - txt.count('h') - txt.count('i') - txt.count('j') - txt.count('k') - txt.count('l') - txt.count('m') - txt.count('n') - txt.count('o') - txt.count('p') - txt.count('q') - txt.count('r') - txt.count('s') - txt.count('t') - txt.count('u') - txt.count('v') - txt.count('w') - txt.count('x') - txt.count('y') - txt.count('z')]
    return new


    #def split_words(txt):
    #    return txt.split()
