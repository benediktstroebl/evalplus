
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
    # keep track of the number of consonants seen so far
    consonants_count = 0
    # iterate through the string and keep track of the words
    words = []
    for char in s:
        # if the char is a consonant, increment the consonants_count
        if char.isdigit() or char.isalpha():
            consonants_count += 1
        # if the consonants_count is equal to n, add the word to the list
        if consonants_count == n:
            words.append(s[:i] + s[i+1:])
            consonants_count = 0  # reset the consonants_count
    # if the last word doesn't match the condition, append it to the list
    if consonants_count != n:
        words.append(s)
    return words
