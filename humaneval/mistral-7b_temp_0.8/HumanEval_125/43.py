
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
    # Let's do the parsing first
    if txt == "":
        return []
    else:
        new_list = txt.split()
        # Let's do the counting next
        list_of_odd_letters = []
        for char in txt:
            if ord(char) % 2 == 1:
                list_of_odd_letters.append(char)
        return list_of_odd_letters
