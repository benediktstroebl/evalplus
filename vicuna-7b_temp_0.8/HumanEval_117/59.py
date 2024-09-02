
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
    # A dictionary to keep track of the current word and the number of consonants.
    word_count = {}
    
    # A set to store the words which have n consonants.
    result = set()
    
    # A counter variable to keep track of the current word being processed.
    i = 0
    
    # A flag variable to check if the word is empty.
    word_empty = True
    
    for char in s:
        # If the word is empty and the counter is greater than 0,
        # add the current word to the result set and reset the counter.
        if not word_empty and s[i] in word_count and word_count[s[i]] == i:
            result.add(s[i:])
            i = 0
            word_empty = False
        # If the word is empty, increment the counter and check if the word is empty.
        else:
            word_count[s[i]] = i + 1
            i += 1
            word_empty = False
    
    # Add the final word to the result set.
    result.add(s[i:])
    
    return list(result)