
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
    # Create a set to store the consonant characters
    consonants = set(string.ascii_letter for string in string.ascii_letters)
    # Create a list to store the words
    words = []
    # Iterate through the string s
    for i in range(len(s)):
        # Create a variable to store the current consonant count
        consonant_count = 0
        # Iterate through the substring s[i:i+1]
        for j in range(1, len(s) - i + 1):
            # Get the consonant character from the substring
            consonant = s[i+j]
            # Check if the consonant character is in the set of consonant characters
            if consonant in consonants:
                # Increment the consonant count
                consonant_count += 1
            else:
                # Reset the consonant count
                consonant_count = 0
        # If the consonant count is equal to n, then add the word to the list of words
        if consonant_count == n:
            words.append(s[i:i+1])
        # Reset the consonant count if it is not equal to n
        else:
            consonant_count = 0
    return words