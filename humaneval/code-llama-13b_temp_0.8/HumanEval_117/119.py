
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
    # Step 1: define a list
    list_words = []
    # Step 2: iterate through string
    for i in s.split():
        # Step 3: check if word contains n consonants
        # Step 4: if it does, append to list
        consonants = 0
        for j in i:
            if j not in "aeiouAEIOU":
                consonants += 1
        if consonants == n:
            list_words.append(i)
    return list_words
    
