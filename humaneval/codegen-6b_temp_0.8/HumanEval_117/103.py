
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
    # Determine the minimum length of a word to consider
    minimum_length_of_word = n + 1

    # Determine the number of words candidates
    candidate_words_length = len(s.split())

    # Search for words whose length is equal or greater than the required length
    for word_length in range(minimum_length_of_word, candidate_words_length + 1):

        # Search for words whose length is equal or greater than the required length
        for word_index in range(0, candidate_words_length - word_length + 1):

            # If the sentence is not empty
            if s != "":

                # If the word contains n consonants, add it to the candidate list
                if word_length > len(s.split()[word_index + word_length - 1]):
                    candidate_words_list.append(s.split()[word_index : word_index + word_length])

    return candidate_words_list


