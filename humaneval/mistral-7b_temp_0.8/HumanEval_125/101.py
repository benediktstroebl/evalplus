
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
    split_word = txt.split()
    split_word.sort()
    if len(split_word) == 0:
        return txt
    if len(split_word) > 0:
        odd = 0
        for i in split_word:
            if ord(i) % 2 != 0:
                odd += 1
        return odd

