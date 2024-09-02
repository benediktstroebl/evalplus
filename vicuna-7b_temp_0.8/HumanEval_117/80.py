
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
    # check if string is empty or not
    if len(s) == 0:
        return []
    # initialize an empty list to store the words
    words = []
    # iterate over all characters in the string
    for i in range(len(s)):
        # check if current character is a consonant
        if s[i] in "bcdfghjklmnpqrstvwxyz":
            # initialize a variable to store the number of consonants
            num_consonants = 0
            # iterate over all characters in the current word
            for j in range(len(s[i])-1):
                # check if the current character is a consonant
                if s[i+j] in "bcdfghjklmnpqrstvwxyz":
                    num_consonants += 1
                else:
                    num_consonants -= 1
            # if the current word contains n consonants
            if num_consonants == n:
                words.append(s[i:i+len(s[i])-1])
        else:
            words.append(s[i])
    return words