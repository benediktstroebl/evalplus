
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
    # check if s is empty
    if len(s) == 0:
        return []
    # initialize a list to store words
    words = [s]
    # keep track of the number of consonants
    consonants = 0
    # iterate over all characters in the string s
    for i in range(len(s)):
        # if the character is a consonant
        if s[i] in "bcdfghjklmnpqrstvwxyz":
            # increment the number of consonants
            consonants += 1
        else:
            # decrement the number of consonants
            consonants -= 1
            # if the number of consonants is zero, remove the word from the list
            if consonants == 0:
                words.remove(s[:i+1])
    return words