
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
    # empty string should return an empty list
    if not s:
        return []
    
    # split the string into a list of words
    words = s.split()
    
    # initialize the result list
    result = []
    
    # iterate through the words
    for word in words:
        # check if the word is a consonant
        if word.isupper():
            # check if the word contains exactly n consonants
            if len(word) <= n and len(word) >= n:
                # add the word to the result list
                result.append(word)
    
    # return the result list
    return result
