
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
    # create an empty list
    selected_words = []
    # split the string into list of words
    words = s.split()
    # for every word in the word list
    for word in words:
        # create a variable consonants that stores the number of consonants in the word
        consonants = 0
        # for every character in the word
        for char in word:
            # if the character is not in a list of vowels
            if char.lower() not in ['a', 'e', 'i', 'o', 'u']:
                # increment the consonants counter
                consonants += 1
        # if the number of consonants is equal to n add the word to the list
        if consonants == n:
            selected_words.append(word)
    return selected_words
