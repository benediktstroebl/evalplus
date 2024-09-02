
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
    # A dictionary that maps each letter to its frequency in the string
    freq = {}
    for i in s:
        freq[i] = freq.get(i, 0) + 1
    
    # The list of all words in the string
    words = s.split()
    
    # The list of words that contain exactly n consonants
    result = []
    
    # Loop through each word in the list of words
    for i in range(len(words)):
        # Keep track of the number of consonants in the current word
        consonants = 0
        for word in words[:i]:
            if word.isalpha() and word.islower():
                freq[word] = freq.get(word, 0) + 1
                if freq[word] == n:
                    consonants += 1
        # If the current word contains exactly n consonants, add it to the result list
        if consonants == n:
            result.append(words[i])
    
    return result
