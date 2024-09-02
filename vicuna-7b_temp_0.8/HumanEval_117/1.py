
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
    # Create a new list to hold the words
    words = []
    # Iterate through the string, character by character
    for i in range(len(s)):
        # Initialize a variable to store the previous consonant
        prev_con = ''
        # Create a new variable to store the current consonant
        con = s[i].lower()
        # If the current character is a consonant, update the previous consonant
        if con in 'bcdfghjklmnpqrstvwxyz':
            prev_con += con
        # If the current character is a vowel, start a new word
        elif con in 'aeiou':
            # If the previous character was a consonant, store the current word
            if prev_con:
                words.append(prev_con)
                # Reset the previous consonant to ''
                prev_con = ''
            # If the previous character was a vowel, there is no word to store
            # so start a new word
            else:
                words.append('')
        # If the current character is neither a consonant nor a vowel,
        # store the current word and move to the next character
        else:
            words.append(s[i:i+1])
            # Reset the current character to ''
            i += 1
    # If the string is empty, return an empty list
    if not words:
        return []
    # If the string has exactly n consonants, return the words
    if len(prev_con) == n:
        return words
    # If the string has more than n consonants, return an empty list
    else:
        return []
