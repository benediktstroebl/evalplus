
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
    txt = str(txt)
    if txt.count(" ") == 0 and txt.count(",") == 0:
        count = 0
        for i in range(len(txt)):
            if txt[i] == "a":
                count += 1
            elif txt[i] == "e":
                count += 1
            elif txt[i] == "i":
                count += 1
            elif txt[i] == "o":
                count += 1
            elif txt[i] == "u":
                count += 1
            elif txt[i] == "y":
                count += 1
        return count
    if txt.count(" ") == 0:
        return [txt]
    if txt.count(",") == 0:
        return [txt]
    return txt.split()
