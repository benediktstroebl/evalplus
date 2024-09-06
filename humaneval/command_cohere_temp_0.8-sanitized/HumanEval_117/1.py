def select_words(s, n):
    consonants = 'bcdfghjklmnpqrstvwxyz'
    words = s.split()
    result = [word for word in words if len(word) == n and sum(1 for c in word if c in consonants) == n]
    return result if result else []