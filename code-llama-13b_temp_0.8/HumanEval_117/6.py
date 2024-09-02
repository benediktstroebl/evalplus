
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
    # if s is empty return an empty list
    if len(s) == 0:
        return []
    # if the number of consonants is 0, return an empty list
    if n == 0:
        return []
    
    # create a list of all the words in the given string
    s = s.split()
    
    # create a list to store words with n consonants
    result = []
    
    # create a string of all consonants
    consonants = 'bcdfghjklmnpqrstvwxyz'
    
    # iterate over all words in the given string
    for word in s:
        
        # if the word contains n consonants, add it to the result
        if len([c for c in word if c in consonants]) == n:
            result.append(word)
            
    return result

