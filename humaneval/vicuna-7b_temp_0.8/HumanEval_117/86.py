
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
    # Create a list to store the selected words
    selected_words = []
    # Iterate through each character in the string s
    for i, c in enumerate(s):
        # If the current character is a letter, continue the loop
        if c.isalpha():
            continue
        # If the current character is a consonant, append the current word
        # to the selected_words list and reset the current position
        selected_words.append(s[i:i+1])
        i += 1
        # If the current position is at the end of the string, reset the
        # current position to the start of the string and continue the loop
        if i == len(s):
            i = 0
    return selected_words
