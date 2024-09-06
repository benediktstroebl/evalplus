def count_consonants(word):
    """
    This function counts the number of consonants in a given word.
    A consonant is a letter that is not a vowel (letters in 'aeiou')
    """
    num_consonants = 0
    for char in word:
        if char.lower() not in 'aeiou':
            num_consonants += 1
    return num_consonants
def select_words(s, n):
    """
    This function selects words from a string that contain exactly 'n' consonants.
    Returns an empty list if no words are found.
    """
    words = s.split()  # Split the input string into a list of words
    filtered_words = [word for word in words if count_consonants(word) == n]
    return filtered_words