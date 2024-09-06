
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
    # Find all spaces in the string
    spaces = re.findall(r'[ \t\n\r]+', s)
    
    # Create a set of all letters in the string
    letters = set(string.ascii_letters)
    for c in s:
        if c not in letters:
            letters.add(c)
    
    # Create a list of words in the string
    words = s.split()
    
    # Keep track of the number of consonants in each word
    consonants = 0
    
    # Loop through each word
    for word in words:
        # Keep track of the number of consonants in the current word
        consonants += len(filter(lambda x: x.isdigit(), word))
    
        # If the number of consonants is equal to the desired value
        if consonants == n:
            # Add the current word to the list of words
            result.append(word)
    
    # Return the list of words
    return result