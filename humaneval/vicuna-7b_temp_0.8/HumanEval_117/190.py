
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
    # Remove leading and trailing spaces from the input string s
    s = s.lstrip()
    s = s.rstrip()
    
    # Create an empty list to store the results
    result = []
    
    # Loop through the characters in s
    for i in range(len(s)):
        # If the current character is a consonant
        if s[i] in "bcdfghjklmnpqrstvwxyz":
            # Replace the current character with a space
            s = s.replace(s[i], " ")
            # Add the current word to the result list
            result.append(s)
        elif s[i] in "aeiou":
            # If the current character is a vowel, append the current word to the result list
            result.append(s)
    
    # Return the list of words that have exactly n consonants
    return result
