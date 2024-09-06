
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
    # Step 1: split s into a list of strings.
    str_lst = s.split()

    # Step 2: declare an empty list.
    list_of_words = []

    # Step 3: write a for loop to traverse str_lst.
    # Step 4: write an inner while loop to traverse each string in str_lst.
    # Step 5: write an if statement to check if the number of consonants equals n.
    # Step 6: append the word to the list of words.
    # Step 7: return the list of words.

    return list_of_words

