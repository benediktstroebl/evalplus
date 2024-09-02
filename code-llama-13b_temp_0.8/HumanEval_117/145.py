
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
    # your code here
    # Your code here. 
    # As a first step, try writing code that returns a list of all words from string s.
    # This would be a good place to start:
    # words = s.split()
    # print(words)

    # Note that you will have to define a function that counts the number of consonants in a word.
    # You can do this with a for loop, a list, and a dictionary.

    def get_consonant_count(word):
        consonants = "bcdfghjklmnpqrstvwxz"
        consonant_count = 0

        for char in word:
            if char in consonants:
                consonant_count += 1

        return consonant_count
    
    words = s.split()
    consonant_words = []

    for word in words:
        if get_consonant_count(word) == n:
            consonant_words.append(word)

    return consonant_words
