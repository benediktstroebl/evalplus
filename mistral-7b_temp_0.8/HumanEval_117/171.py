
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

    def is_consonant(char):
        return char not in "aeiou"

    # Initialize empty list
    result = []

    # Step through the string, character by character
    for i in range(len(s)):
        # Keep track of current word
        word = ""

        # Keep track of number of consonants in current word
        consonants = 0

        # While the current word has not been completed
        while i < len(s) and word not in result:
            # If we are not on a space
            if s[i] != " ":
                # If we have a consonant
                if is_consonant(s[i]):
                    consonants += 1
                # If we have reached the number of consonants we need
                if consonants == n:
                    # Add this word to the list
                    result.append(word)
                    # Break the loop
                    break
                # Add the letter to the current word
                word += s[i]
            # If we
