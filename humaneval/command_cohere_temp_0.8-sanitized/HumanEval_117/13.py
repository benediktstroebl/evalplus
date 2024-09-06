def count_consonants(word):
    """
    Counts the number of consonants in a word
    """
    word = word.lower()
    total = 0
    for char in word:
        if char in 'bcdfghjklmnpqrstvwxyz':
            total += 1
    return total
def select_words(s, n):
    """
    Selects words from a string that contain exactly n consonants
    """
    words = s.split()
    result = []
    for word in words:
        consonant_count = count_consonants(word)
        if consonant_count == n:
            result.append(word)
    return result