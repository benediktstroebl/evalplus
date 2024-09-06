def count_consonants(word):
    """
    This function counts the number of consonants in a given word.
    A consonant is a letter that is not a vowel (uppercase or lowercase)
    or the hyphen ('-').
    """
    consonants = 0
    for char in word:
        if char.isalpha():
            if char in 'QWERTYUIOP{}|':
                consonants += 1
        elif char == '-':
            consonants += 1
    return consonants
def select_words(s, n):
    """
    This function selects words from a string that contain exactly 'n' consonants.
    If the string is empty or the number of consonants is less than 'n',
    an empty list is returned.
    """
    words = []
    word_args = [s.split(' ')]
    for i in range(len(word_args[0])):
        word = word_args[0][i]
        if count_consonants(word) == n:
            words.append(word)
    return words