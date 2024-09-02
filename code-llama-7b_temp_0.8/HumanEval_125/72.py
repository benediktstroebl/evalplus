
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

    # only if there is a comma in the string, split it.
    if "," in txt:
        return txt.split(",")

    # only if there is no comma in the string, count the number of lower-case letters with odd order in the alphabet.
    elif "," not in txt:
        count = 0
        for char in txt:
            if char.isalpha():
                if ord(char) % 2 != 0:
                    count += 1
        return count

