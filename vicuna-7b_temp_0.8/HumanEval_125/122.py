
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
    txt = txt.replace(" ", ",")
    txt = txt.split(",")
    count = [ord(letter) for letter in txt]
    count = [chr(x) for x in count if x > ord('a') and x < ord('z')]
    if count:
        return txt[count.index(min(count, key=ord))]
    else:
        return txt
