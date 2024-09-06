
def select_words(s, n):
    """Given a string s and a natural number n, you have been tasked to implement 
    a function that returns a list of all words from string s that contain exactly 
    n consonants, in order these words appear in the string s.
    If the string s is empty then the function should return an empty list.
    Note: you may assume the input string contains only letters and spaces.
    Examples:
    select_words("Mary had a little lamb", 4) ==> ["little"]
    select_words("Mary had a little lamb", 3) ==> ["Mary", "lamb"]
    select_words("simple white space", 2) ==> []
    select_words("Hello world", 4) ==> ["world"]
    select_words("Uncle sam", 3) ==> ["Uncle"]
    """
    # Try to use pythonic way to solve this problem
    # use re to check if a word is valid
    # if a word is valid, return it
    # if a word is invalid, check if it ends with a consonant and if it does, 
    # append it to a list and continue checking the next word
    # repeat this process until we have a valid word or all words have been checked
    result = []
    for word in s.split():
        if "bcdfghjklmnpqrstvwxz"[0] + "abcdefghijklmnpqrstuvwxyz"[1:] in word:
            result.append(word)
    return result