def count_consonants(word):
    """
    This function counts the number of consonants in a given word.
    """
    word = word.lower()
    total = 0
    for c in word:
        if c in 'bcdfghjklmnpqrstvwxyz':
            total += 1
    return total
def select_words(s, n):
    """
    This function selects words from a string that contain exactly n consonants.
    """
    words = s.split()
    result = []
    for word in words:
        consonant_count = count_consonants(word)
        if consonant_count == n:
            result.append(word)
    return result