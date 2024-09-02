
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
    # Add your code here
    # Let's use a dictionary to count the number of consonants in each word
    consonant_count = {}
    for char in s:
        if char.isalpha():
            if char.islower():
                consonant_count[0] += 1
            elif char.isupper():
                consonant_count[1] += 1
            elif char.isdigit():
                consonant_count[2] += 1
            else:
                consonant_count[3] += 1
    
    # Initialize an empty list to store the words
    result = []
    
    # Iterate through the words in the string s
    for i in range(0, len(s), n):
        # If the current word is not empty
        if i + n < len(s):
            # Check if the word contains exactly n consonants
            if len(s[i:i + n]) == n and all(c in consonant_count[count] for count in range(1, n+1) for c in s[i:i+n]):
                # If yes, add the word to the result list
                result.append(s[i:i+n])
    
    return result
