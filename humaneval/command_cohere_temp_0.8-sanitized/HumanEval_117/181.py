def count_consonants(word):
    counts = {char: 1 for char in word if char in 'bcdfghjklmnpqrstvwxyz'}
    return sum(counts.values())
def select_words(s, n):
    words = s.split()
    result = []
    for word in words:
        if count_consonants(word) == n:
            result.append(word)
    return result