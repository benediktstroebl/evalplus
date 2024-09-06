
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
    # initialize an empty list to store the words
    words = []
    # iterate through all characters in the string
    for i in range(len(s)):
        # if current character is a consonant
        if s[i] in 'bcdfghjklmnpqrstvwxyz':
            # increment a counter variable
            consonant_counter += 1
        # if the current character is a space
        elif s[i] == ' ':
            # check if the counter variable is equal to n
            if consonant_counter == n:
                # add current word to the list of words
                words.append(s[i:i+len(s[i])])
                # reset the counter variable
                consonant_counter = 0
        # if the current character is a vowel
        else:
            # check if the counter variable is equal to n
            if consonant_counter == n:
                # add current word to the list of words
                words.append(s[i:i+len(s[i])])
                # reset the counter variable
                consonant_counter = 0
    return words
