
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
    # Pseudocode:
    # if string is empty, return empty list
    # if n < 1, return empty list
    # split the string at white spaces, store as list of words
    # for each word in the list of words
    #     create counter for consonants
    #     for each char in the word
    #         if char is a consonant, counter goes up
    #     if counter == n, add to list of words containing n consonants
    # return the list of words
    if not s:
        return []
    if n < 1:
        return []
    words = s.split()
    words_with_n_consonants = []
    for word in words:
        consonant_counter = 0
        for char in word:
            if char not in 'aeiouAEIOU':
                consonant_counter += 1
        if consonant_counter == n:
            words_with_n_consonants.append(word)
    return words_with_n_consonants
