
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
    # Find the index of the first consonant in the string
    i = 0
    while i < len(s) and s[i] == " ":
        i += 1
    if i == len(s):
        return []
    # Initialize a list to store the words
    words = [s[i:i+1]]
    # Keep track of the number of consonants in the current word
    consonant_count = 0
    # Find the index of the next consonant
    j = i+1
    while j < len(s) and s[j] == " ":
        j += 1
    # For each word in the list
    for word in words:
        # For each character in the word
        for c in word:
            # Increment the consonant count
            consonant_count += 1
            # If the word has the correct number of consonants
            if consonant_count == n:
                # Add the word to the list
                words.append(word)
                # Reset the consonant count
                consonant_count = 0
        # If there are more words in the list
        if j < len(s):
            # Initialize the index of the next consonant
            j = len(s) + 1
    return words