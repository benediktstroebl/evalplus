
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
    # input: string and an integer
    # return: a list of all words from string s that contain exactly n consonants, in order these words appear in the string s

    # use a list to store all the words with n consonants
    words_with_n_consonants = []

    # start at index 0 and iterate to the end of the string
    for i in range(len(s)):
        # if the current letter is a consonant
        if s[i] != " ":
            # add the current word to the list
            words_with_n_consonants.append(s[i])

    # return the list of words with n consonants
    return words_with_n_consonants


