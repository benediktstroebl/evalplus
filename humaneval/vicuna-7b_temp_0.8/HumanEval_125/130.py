
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
    if not txt:
        return 0
    elif txt.lower() in string.punctuation:
        return txt.split(",")
    else:
        wordlist = txt.split()
        for i in range(len(wordlist)):
            if len(wordlist) == 1:
                return 1
            if wordlist[i].lower() in string.punctuation:
                return 1
        if wordlist[-1] == " ":
            return 1
        else:
            return 0
