
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
    # Create a list to store the selected words
    selected_words = []
    
    # Iterate over the string using slicing
    for i in range(0, len(s), n):
        # Check if the substring contains exactly n consonants
        if (s[i:i+n] == "".join([c for c in "cvcvc" if c in s[i:i+n]])) and (s[i:i+n] != "".join([c for c in "ccc" if c in s[i:i+n]])):
            # If yes, add the substring to the selected words list
            selected_words.append(s[i:i+n])
    
    return selected_words
