
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
    # Start by making a copy of the original string so that we don't modify the original
    # We will use this copy to check if the string is empty or not
    s_copy = s.copy()
    words = s_copy.split()
    
    # Create an empty list to store the words
    result = []
    
    # Loop through the words and check if it contains the specified number of consonants
    for i in range(len(words)):
        consonants = "bcdfghjklmnpqrstvwxyz"
        if len(set(words[i]).intersection(consonants)) == n:
            result.append(words[i])
    
    return result