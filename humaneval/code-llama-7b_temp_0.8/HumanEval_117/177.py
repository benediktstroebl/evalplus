
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
    # Create a dictionary with keys = letters and values = 1
    vowels = "aeiou"
    # Create a dictionary with keys = letters and values = 1
    consonants = "".join( [l for l in string.ascii_lowercase if l not in vowels] )
    # Create a dictionary with keys = letters and values = 1
    d_consonants = {k: 1 for k in consonants}
    # Create a dictionary with keys = letters and values = 1
    d_vowels = {k: 1 for k in vowels}
    # Create a list with n elements, all initialized to 0
    result = []
    words = s.lower().split(" ")

    for word in words:
        word_cons = [l for l in word if l in d_consonants]
        word_vowels = [l for l in word if l in d_vowels]
        # Check the number of consonants is equal to the number of vowels in the word
        if len(word_cons) == n and len(word_vowels) == n:
            # Append the word to the result list
            result.append(word)

    return result
