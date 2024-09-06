
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
    # find all consonants in the string
    consonants = [c for c in string.ascii_letters if string.isalpha(c)]
    # find all words in the string
    words = string.split(s)
    # initialize a list to store the selected words
    selected_words = []
    # iterate over the words
    for word in words:
        # check if the word contains exactly n consonants
        if len(set(word).intersection(consonants)) == n:
            # if the word is selected, append it to the selected_words list
            selected_words.append(word)
    return selected_words