
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
    txt = txt.replace(" ", "")
    txt = txt.replace(",", "")
    # Convert txt to a set of characters
    txt_set = set(txt)
    # Remove duplicates from txt_set
    txt_set = txt_set.union(txt_set)
    # Get the list of unique characters in txt_set
    txt_set = sorted(txt_set)
    # Get the length of txt
    txt_length = len(txt)
    # Get the total number of lower-case letters
    txt_lower_case = 0
    # Iterate through the txt_set
    for char in txt_set:
        txt_lower_case += ord(char)
    # If txt is empty return 0
    if txt_length == 0:
        return 0
    # Get the last letter of txt
    last_letter = txt[-1]
    # Get the sum of the number of lower-case letters of txt
    txt_lower_case += len(txt)
    # If last letter is an odd letter
    if ord(last_letter) % 2 != 0:
        return txt_lower_case
