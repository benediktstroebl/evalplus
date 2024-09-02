
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
    # Set the input to a list, and run a for loop to change all the letters to lowercase
    s = s.lower().split()

    # Create an empty list for the words with the correct amount of consonants
    list_of_words = []

    # Loop through the list of words in the input string
    for x in s:

        # Count the number of consonants in each word
        consonant_count = 0
        for letter in x:
            if letter not in ['a', 'e', 'i', 'o', 'u']:
                consonant_count += 1

        # If the number of consonants equals the input, add it to the list
        if consonant_count == n:
            list_of_words.append(x)
    return list_of_words
