def count_consonants(word):
    """
    This function counts the number of consonants in a given word.
    consonants are all the letters that are not vowels (uppercase and lowercase)
    """
    consonants = ['J', 'K', 'G', 'B', 'C', 'D', 'T', 'P', 'Q', 'S', 'X', 'Z', 'Ch', 'Th', 'Ph', 'Kw', 'Wh', 'Zz', 'Zh']
    count = 0
    for char in word:
        if char in consonants:
            count += 1
    return count
def select_words(s, n):
    """
    This function takes a string s and an integer n, and returns a list of all words from string s that contain exactly n consonants, in order these words appear in the string s.
    If the string s is empty then the function should return an empty list.
    """
    words = []
    for word in s.split():
        consonant_count = count_consonants(word)
        if consonant_count == n:
            words.append(word)
    return words