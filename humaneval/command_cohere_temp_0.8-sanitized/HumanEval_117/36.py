def count_consonants(word):
    """
    Function to count the number of consonants in a word
    """
    ct = 0
    for c in word:
        if c in 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ':
            ct += 1
    return ct
def select_words(s, n):
    """
    Selects words from a string that contains exactly n consonants
    """
    words = s.split()
    result = []
    for word in words:
        ct = count_consonants(word)
        if ct == n:
            result.append(word)
    return result