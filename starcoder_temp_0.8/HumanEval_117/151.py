
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

    # Make a list from the input string
    words = s.split()

    # Make a list of tuples
    #   (word, number of consonants in the word)
    word_tuples = []
    for word in words:
        # Remove all non-letters
        #   and convert to lower case
        word = ''.join(ch for ch in word if ch.isalpha()).lower()
        word_tuples.append((word, count_consonants(word)))

    # Make a list of words that have n consonants
    words_with_n_consonants = []
    for word, count in word_tuples:
        if count == n:
            words_with_n_consonants.append(word)

    # Sort the list of words in alphabetical order
    words_with_n_consonants.sort()

    return words_with_n_consonants

