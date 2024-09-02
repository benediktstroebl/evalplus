
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
    
    if " " not in txt and "," not in txt:
        letters = []
        for i in range(26):
            letters.append(chr(i+ord("a")))
        counter = 0
        for i in range(1,len(letters)+1,2):
            if letters[i] in txt:
                counter += 1
        return counter
    else:
        return txt.split(" ")
