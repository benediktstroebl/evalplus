def count_consonants(word):
    """
    Helper function to count the number of consonants in a word.
    """
    word = word.lower()
    total = 0
    for c in word:
        if c in 'bcdfghjklmnpqrstvwxyz':
            total += 1
    return total
def select_words(s, n):
    """
    Returns a list of all words from string s that contain exactly n consonants.
    """
    # Split the input string s into a list of words based on spaces
    words = s.split()

    # Filter words based on the number of consonants being exactly n
    words_n_consonants = filter(lambda word: count_consonants(word) == n, words)

    # Convert the list of words back to a string for the answer (or empty string if list is empty)
    result = ' '.join(words_n_consonants)

    return result