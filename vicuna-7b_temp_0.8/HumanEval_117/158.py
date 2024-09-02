
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
    # check if the string is empty or not
    if len(s) == 0:
        return []
    else:
        # initialize an empty list to store the words
        words = []
        # initialize a variable to count the number of consonants
        consonants = 0
        # initialize a variable to check if the current character is a consonant
        is_consonant = True
        # iterate through each character in the string s
        for char in s:
            # check if the current character is a consonant or not
            if char.isalpha() and char.islower():
                # if the current character is a consonant, reset the is_consonant variable
                is_consonant = False
            elif is_consonant:
                # increment the consonants variable
                consonants += 1
            else:
                # if the current character is a vowel, add it to the words list
                words.append(char)
                # reset the is_consonant variable
                is_consonant = True
        # add the remaining words to the list
        words.extend(s[consonants:])
        return words
