
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
    # Return an empty list if there are no words in the string
    if s == "":
        return []

    # Create an empty list to store the selected words
    selected_words = []

    # Define a function to check if a character is a vowel
    vowels = "aeiou"

    # Loop through each character in the string
    for i in range(len(s)):
        # Check if the current character is a vowel
        if s[i] in vowels:
            # If it is a vowel, increment the count
            n += 1

            # If the count is now equal to the number of consonants required,
            # add the word to the selected words list and reset the count
            if n == n:
                selected_words.append(s[i:i + 1])
                n = 0

    # Return the selected words list
    return selected_words
