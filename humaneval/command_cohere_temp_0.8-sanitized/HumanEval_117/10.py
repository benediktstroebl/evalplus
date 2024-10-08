def count_consonants(word):
    """Count consonants in a word"""
    word = word.lower()
    total = 0
    for char in word:
        if char in "bcdfghjklmnpqrstvwxyz":
            total += 1
    return total
def select_words(s, n):
    """Return list of words with exactly n consonants"""
    words = s.split()
    result = []
    for word in words:
        count = count_consonants(word)
        if count == n:
            result.append(word)
    return result