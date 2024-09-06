def count_consonants(word):
    """
    This function counts the number of consonants in a given word.
    consonants are letters that are not vowels from the English alphabet
    """
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    count = 0
    for letter in word:
        if letter not in vowels:
            count += 1
    return count
def select_words(s, n):
    """
    This function takes a string s and an integer n, returns a list of all words from string s that contain exactly n consonants, in order these words appear in the string s.
    If the string s is empty then the function should return an empty list.
    """
    words = []
    for space in s.split():
        if count_consonants(space) == n:
            words.append(space)
    return words