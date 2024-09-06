
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
    # Create a dictionary to count consonant occurrences
    consonant_count = {}
    for i in range(len(s)):
        consonant_count[s[i]] = consonant_count.get(s[i], 0) + 1
    
    # Create a list to store the selected words
    selected_words = []
    
    # Loop through the string and find the first instance of a consonant
    for i in range(len(s)):
        if s[i] in consonant_count:
            selected_words.append(s[i])
            break
    
    # Loop through the remaining characters and append any consonants to the list
    for j in range(len(s)):
        if j != i:
            if s[j] in consonant_count:
                selected_words.append(s[j])
    
    return selected_words