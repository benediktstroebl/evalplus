
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
    if " " in txt:
        return txt.split(" ")
    elif "," in txt:
        return txt.split(",")
    else:
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        res = []
        for i in range(len(alphabet)):
            if txt[i] in alphabet:
                if alphabet.find(txt[i]) % 2 == 1:
                    res.append(txt[i])
        return res
    

