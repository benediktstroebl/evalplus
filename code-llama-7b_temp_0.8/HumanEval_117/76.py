
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
    # Convert to lower case
    s = s.lower()
    # Split the string into a list of words
    s = s.split()
    # Iterate through each word and split into list of letters
    for i in range(len(s)):
        s[i] = list(s[i])
    # Remove all words that have less or more than n consonants
    for i in range(len(s)):
        count = 0
        for c in s[i]:
            if c in "aeiou":
                continue
            else:
                count += 1
        if count != n:
            s.remove(s[i])
    # Return the list of words that have n consonants
    return s

