def count_consonants(word):
    """
    Counts the number of consonants in a word.
    A consonant is a letter that is not a vowel (uppercase or lowercase)
    """
    num_consonants = 0
    for char in word:
        if char.lower() not in 'aeiou':
            num_consonants += 1
    return num_consonants
def select_words(s, n):
    """
    Finds all words in 's' that contain exactly 'n' consonants.
    Returns an empty list if no words are found.
    """
    words = []
    word_inds = []
    s_ind = 0
    for ind, char in enumerate(s):
        if char == ' ':
            if count_consonants(s[s_ind:ind]) == n:
                words.append(s[s_ind:ind].strip())
            s_ind = ind
        elif char == ' ':
            word_inds.append(ind)
    # Handle the last word
    if count_consonants(s[s_ind:]) == n:
        words.append(s[s_ind:].strip())
    return words if words else []