
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
    # Check if the string is empty or not
    if len(s) == 0:
        return []
    
    # Create a set of all letters in the string
    char_set = set(s)
    
    # Create a list to store the words
    words = []
    
    # Loop through all characters in the string
    for i, c in enumerate(s):
        # Check if the current character is a consonant
        if c.isalpha() and c.islower() or c.isalpha() and c.isupper():
            # If the set of characters in the current word is different from the
            # set of characters in the original string, append the current word
            # to the list of words
            if len(set(words + [c])) == len(char_set):
                words.append(words[words.index(c)])
        
    return words
