def count_consonants(word):
    """
    Counts the number of consonants in a word
    """
    word = word.lower()
    total = 0
    for char in word:
        if char in "bcdfghjklmnpqrstvwxyz":
            total += 1
    return total
def select_words(s, n):
    """
    Returns a list of words from string s that contain exactly n consonants 
    in order these words appear in the string s
    """
    if len(s) == 0:
        return []
    words = s.split()
    result = []
    for word in words:
        consonant_count = count_consonants(word)
        if consonant_count == n:
            result.append(word)
    return result