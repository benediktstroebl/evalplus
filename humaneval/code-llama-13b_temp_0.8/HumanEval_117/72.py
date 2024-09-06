
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
    # Step 1: split the string into words 
    # Step 2: loop over the words 
    # Step 3: check how many consonants are in each word 
    # Step 4: add the word to the result if it satisfies the condition 
    # Return the result 

    words = s.split()
    result = []
    vowels = ['a', 'e', 'i', 'o', 'u']
    
    for word in words:
        consonants = 0
        for char in word:
            if char not in vowels:
                consonants += 1
        if consonants == n:
            result.append(word)
    return result
