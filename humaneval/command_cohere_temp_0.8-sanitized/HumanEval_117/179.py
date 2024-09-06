def select_words(s, n):
    consonants = 'bcdfghjklmnpqrstvwxyz'
    words = s.split()  # Split the string into words on spaces
    
    result = [word for word in words if len(set(word).intersection(consonants)) == n]
    
    return result if result else []