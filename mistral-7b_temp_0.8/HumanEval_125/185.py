
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
    # store the output in a variable
    output = []

    # loop over all the characters in the txt
    for char in txt:
        # check if the char is whitespace
        if char.isspace():
            # if so, add the previous word to the output list
            output.append(txt[:txt.index(char)])
            # reset txt to the part after the whitespace
            txt = txt[txt.index(char)+1:]
        # otherwise, add the char to the end of txt
        else:
            txt += char

    # if txt is not empty, append it to the output list
    if txt:
        output.append(txt)

    # return the output list
    return output

