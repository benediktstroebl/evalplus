
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
    # Split string into list of words
    split_string = s.split()

    # List to store words of length n
    n_words = []

    # Loop through each word
    for word in split_string:
        # List to store consonants in current word
        consonants = []

        # Loop through each letter in current word
        for letter in word:
            # Check if letter is not a vowel
            if letter not in "aeiouAEIOU":
                # Add letter to list of consonants
                consonants.append(letter)

        # Check if word has exactly n consonants
        if len(consonants) == n:
            # Add word to list of n-consonant words
            n_words.append(word)

    return n_words

