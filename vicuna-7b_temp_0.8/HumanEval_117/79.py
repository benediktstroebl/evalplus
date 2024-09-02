
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
    # Use a dictionary to keep track of the last n consonants encountered
    last_n = {}
    for i, c in enumerate(s):
        if c.is_vowel():
            continue
        if c in last_n:
            last_n[c] += 1
        else:
            last_n[c] = 1
    
    # Create a list of all words from the string
    words = s.split()
    
    # Iterate over the words and filter out those with fewer than n consonants
    result = []
    for word in words:
        if len(set(word)) >= n:
            result.append(word)
    
    return result