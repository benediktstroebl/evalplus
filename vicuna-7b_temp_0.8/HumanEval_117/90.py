
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
    # The initial check
    if s == "":
        return []
    
    # The rest of the check
    if n <= 0:
        return []
    
    # Starting at the index of the first consonant
    i = 0
    
    # Finding the end of the word
    j = i + 1
    while j < len(s) and s[j] == " ":
        j += 1
    word = s[i:j]
    
    # If the word contains n consonants, return it
    if len(word) == n:
        return [word]
    
    # If the word doesn't contain n consonants, find the last consonant in the word
    while j < len(s) and s[j] == " ":
        j += 1
    while j < len(s) and s[j] == " ":
        j += 1
    last_consonant = s[j]
    
    # If the word ends with n consonants, return the word
    if len(word) == n:
        return [word]
    
    # If the word doesn't end with n consonants, add the last consonant to the word and find the next consonant
    word += last_consonant
    i = j + 1
    while j < len(s) and s[j] == " ":
        j += 1
    while j < len(s) and s[j] == " ":
        j += 1
    next_consonant = s[j]
    
    # Keep adding the last consonant to the word until the word contains n consonants
    while True:
        word += last_consonant
        i += 1
        while i < len(s) and s[i] == " ":
            i += 1
        while i < len(s) and s[i] == " ":
            i += 1
        next_consonant = s[i]
        if len(word) == n:
            return [word]
        last_consonant = next_consonant
