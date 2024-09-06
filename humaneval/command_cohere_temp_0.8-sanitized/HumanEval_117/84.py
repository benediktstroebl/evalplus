def select_words(s, n):
    consonants = {'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'}
    words = s.split()
    result = [word for word in words if len(word) >= n and len(set(word).intersection(consonants)) == n]
    return result if result else []