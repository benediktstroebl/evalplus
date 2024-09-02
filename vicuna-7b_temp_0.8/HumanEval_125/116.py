
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
    txt = txt.lower() #convert to lowercase
    txt = txt.split() #split the text on whitespace
    if not txt:
        txt = [ord(letter) for letter in "abcdefghijklmnopqrstuvwxyz"]
        txt.insert(0, txt[1])
    else:
        txt = txt[::2] + [txt[1::2].lower()]
    txt = [re.sub(r"[aeiou]", '', word) for word in txt]
    txt = [word for word in txt if len(word) > 2]
    return txt
