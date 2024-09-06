
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
    split_txt = txt.split()
    split_lst = []
    for word in split_txt:
        if word.isalpha():
            for ch in word:
                if ch.isalpha() and ord(ch) % 2 == 1:
                    split_lst.append(word)
    return split_lst

