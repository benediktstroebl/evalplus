
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
    # Create a list to store the words
    words = []
    # Create a variable to store the current index
    current_index = 0
    # Loop through the string s
    for i in range(len(s)):
        # Check if the current character is a consonant
        if s[i] in "bcdfghjklmnpqrstvxz":
            # Increment the current index
            current_index += 1
        elif s[i] == " ":
            # If the current index is equal to n, append the word to the list
            if current_index == n:
                words.append(s[current_index:])
                # Set the current index to 0
                current_index = 0
    # If the current index is not equal to n, append the word to the list
    if current_index != n:
        words.append(s[current_index:])
    # Return the list of words
    return words
