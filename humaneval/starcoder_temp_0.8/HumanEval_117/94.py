
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
    # Your code here
    # To create a list of consonants we first create an empty list
    consonants = []
    # Then we loop through all characters in s
    for character in s:
        # If the character is a space we skip it
        if character == " ":
            continue
        # If the character is a vowel we append it to the list of vowels
        elif character in ["a", "e", "i", "o", "u", "y"]:
            vowels.append(character)
        # Otherwise we add it to the list of consonants
        else:
            consonants.append(character)
    # We finally return the first n words in s
    return s.split()[0:n]

