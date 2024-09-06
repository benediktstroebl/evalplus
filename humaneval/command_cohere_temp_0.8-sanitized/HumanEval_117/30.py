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
    Returns a list of all words from string s that contain exactly n consonants, 
    in order these words appear in the string s.
    If the string s is empty then the function should return an empty list.
    """
    # Ensure the input string is not empty and the number of consonants to find is a natural number.
    if not s or not isinstance(n, int) or n < 0:
        return []

    words = s.split()
    result = []

    for word in words:
        consonant_count = count_consonants(word)
        if consonant_count == n:
            result.append(word)

    return result