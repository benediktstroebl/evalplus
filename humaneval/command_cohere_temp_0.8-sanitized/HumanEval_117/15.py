def count_consonants(word):
    consonants = sum(1 for c in word if c in 'bcdfghjklmnpqrstvwxyz')
    return consonants
def select_words(s, n):
    words = s.split()
    result = [word for word in words if count_consonants(word) == n]
    return result