def count_consonants(word):
    """Count consonants in a word"""
    word = word.lower()
    total = 0
    for char in word:
        if char != 'a' and char != 'e' and char != 'i' and char != 'o' and char != 'u' and \
           char != 'y' and char != 'h':
            total += 1
    return total
def select_words(s, n):
    """Return list of words containing exactly n consonants"""
    words = []
    for word in s.split():
        consonant_count = count_consonants(word)
        if consonant_count == n:
            words.append(word)
    return words