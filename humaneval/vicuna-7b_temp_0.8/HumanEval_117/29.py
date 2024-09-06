
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
    # check if the input string is empty or not
    if len(s) == 0:
        return []
    # check if the input string is of zero length or not
    if len(s) == 1:
        return [s]
    # check if the input string is of zero length
    if len(s) == 1:
        return [s]
    # check if the number of consonants is less than the length of the string
    if n < len(s):
        return []
    # initialize the result list
    result = []
    # check if the string starts with a consonant
    if s[0] == " ":
        result.append(s[0])
    # check if the string starts with a vowel
    for i in range(1, len(s)):
        if s[i] in "aeiouAEIOU":
            result.append(s[i])
    # check if the string starts with a vowel
    for i in range(1, len(s)):
        if s[i] in "bcdfghjklmnpqrstvwxyz":
            result.append(s[i])
    # check if the string starts with a vowel
    for i in range(1, len(s)):
        if s[i] in "qwertyuiopasdfghjkl":
            result.append(s[i])
    # check if the string starts with a vowel
    for i in range(1, len(s)):
        if s[i] in "zxcvbnmQWERTYUIOPASDFGHJKL":
            result.append(s[i])
    # check if the string starts with a vowel
    for i in range(1, len(s)):
        if s[i] in "zxcvbnmQWERTYUIOPASDFGHJKL":
            result.append(s[i])
    # return the result list
    return result
