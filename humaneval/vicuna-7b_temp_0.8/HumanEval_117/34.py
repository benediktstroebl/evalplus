
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
    # Define a helper function to check the presence of a certain consonant in the string
    def check_consonant(s, i, c):
        if s[i] == c:
            return True
        if i == len(s) - 1:
            return False
        return check_consonant(s, i+1, c) or check_consonant(s, i-1, c)
    
    # Check the length of the string s
    if len(s) == 0:
        return []
    
    # Create an empty list to store the words
    words = []
    
    # Keep track of the last index i of a consonant
    last_cons_index = 0
    
    # Loop through the string s
    for i in range(len(s)):
        # Check if the current character is a consonant
        if check_consonant(s, i, s[i]):
            # If it is, append it to the list of words
            words.append(s[last_cons_index:i])
            # Update the last index i of a consonant
            last_cons_index = i
        else:
            # If it's not, append it to the list of words
            words.append(s[last_cons_index:i+1])
            # Update the last index i of a consonant
            last_cons_index = i + 1
            
    # Append the last word to the list of words
    words.append(s[last_cons_index:])
    
    return words
