def select_words(s, n):
    consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    words = s.split()
    result = [word for word in words if len(set(word).intersection(consonants)) == n]
    return result if result else []