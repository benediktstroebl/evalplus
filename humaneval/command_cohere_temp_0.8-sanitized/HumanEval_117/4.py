def select_words(s, n):
    consonants = 'bcdfghjklmnpqrstvwxyz'
    words = s.split() 
    result = [word for word in words if len(word) >= 3 and len(set(word).intersection(consonants)) == n]
    return result if result else []