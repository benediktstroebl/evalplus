
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
    # This line of code will check if the string is empty, if it is, it will return an empty list.
    if len(s) == 0:
        return []

    # This line of code will create an empty list that will be used to store the words that contain exactly n consonants.
    words = []

    # This line of code will create a variable that will be used to keep track of the number of consonants that are in the current word.
    consonants_count = 0

    # This line of code will create a variable that will be used to keep track of the current word that is being processed.
    current_word = ""

    # This line of code will create a variable that will be used to keep track of the current index that is being processed.
    index = 0

    # This loop will iterate over the string and it will check if the current character is a consonant.
    # If it is, it will add it to the current word.
    # If the current word contains exactly n consonants, it will add it to the list of words.
    # If
