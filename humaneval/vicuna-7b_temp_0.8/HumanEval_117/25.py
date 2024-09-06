
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
    # Check if the input string is empty or not
    if not s:
        return []
    
    # Initialize the empty list to store the words
    words = []
    
    # Check if the length of the string is equal to 1 or not
    if len(s) == 1:
        # If the length of the string is 1, then it contains only one word
        words = [s]
    else:
        # If the length of the string is greater than 1, then iterate through the string
        for i in range(1, len(s)):
            # Find the first consonant in the current word
            consonant = s[i]
            # Find the first consonant in the previous word
            previous_consonant = s[(i-1)%len(s)]
            # If the current consonant is the first letter in the current word or
            # the current word is empty or the previous word is not empty,
            # then add the current word to the list of words
            if (s[i] == consonant) or (s[(i-1)%len(s)] == ' ') or (previous_consonant != ' '):
                words.append(s[i:])
            else:
                # If the current consonant is not the first letter in the current word
                # and the previous word is not empty, then add the previous word to the list of words
                words.append(previous_consonant)
        
    # Return the list of words
    return words