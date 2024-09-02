
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
    # Check if string is empty
    if len(s) == 0:
        return []
    # Create a dictionary to count consonants
    consonants = {}
    # Check if there are more than n consonants
    if sum(map(len, s)) > n:
        return []
    # Create a list to store words
    words = s.split()
    # Iterate through each word
    for word in words:
        # Check if the word is in the dictionary of consonants
        if word in consonants:
            # The word contains n consonants
            return words.remove(word) + [word]
        # Add consonants to the dictionary
        for char in word:
            if char.isalpha():
                consonants[char] = 1
            else:
                consonants[char] += 1
    return []
