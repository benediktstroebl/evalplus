
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

    # Your code goes here
    # You may assume the input string contains only letters and spaces.
    # Use the is_consonant() function below
    # You can use the is_vowel() function below

    is_consonant = {'a', 'e', 'i', 'o', 'u'}
    is_vowel = {'a', 'e', 'i', 'o', 'u'}
    # A list of all words from string s that contain exactly 3 consonants, in order
    words = []
    # A list of all words from string s that contain exactly 4 consonants, in order
    words2 = []
    # A list of all words from string s that contain exactly 5 consonants, in order
    words3 = []

    # This function will extract all words that contain exactly 3 consonants
    # in order these words appear in the string
    for i in s.split():
        if i.count('a') == 3 or i.count('e') == 3 or i.count('i') == 3 or i.count('o
