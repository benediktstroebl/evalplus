def select_words(s, n):
    consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    words = s.split()  # Split the string into words on spaces
    result = [word for word in words if len(word) >= n and sum(1 for char in word if char in consonants) == n]
    return result if result else []