
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
    import re
    # 1
    ls = re.split('[^a-zA-Z]', txt)
    print(ls)
    # 2
    txt = txt.replace(',', '').lower()
    count = 0
    for x in txt:
        if (ord(x) % 2 == 1):
            count += 1
    return count
