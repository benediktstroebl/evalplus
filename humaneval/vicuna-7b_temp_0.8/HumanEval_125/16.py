
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
    txt = txt.strip()
    if txt:
        # split on whitespaces if any
        words = txt.split()
        if not words:
            # if no whitespaces split on commas
            words = txt.split(',')
        return words
    else:
        # if no whitespaces or commas, count lowercase letters with odd order
        count = 0
        for i in range(len(txt)):
            if txt[i].islower() and (ord(txt[i]) % 2) != 0:
                count += 1
        return count
