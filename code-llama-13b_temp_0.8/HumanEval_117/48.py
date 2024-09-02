
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
    # define consonants 
    consonants = "bcdfghjklmnpqrstvwxz" 
    
    # check empty string
    if s == "":
        return []
    
    # split string by whitespace
    s = s.split()
    
    # loop through each word
    result = []
    for word in s:
        
        # word doesn't have n consonants
        if word.lower().count(consonants) != n:
            continue
        
        # check word
        for i in word:
            if i.lower() in consonants:
                result.append(word)
                break
    
    return result


