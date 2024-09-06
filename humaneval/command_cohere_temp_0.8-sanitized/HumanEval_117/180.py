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
    Reimplemented function to select words containing exactly n consonants.
    """
    if not s:
        return []
    words = s.split()
    result = []
    for word in words:
        consonant_count = count_consonants(word)
        if consonant_count == n:
            result.append(word)
    return result