def select_words(s, n):
    consonants = {'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'}
    words = s.split()
    result = []
    for word in words:
        num_consonants = sum(1 for char in word if char in consonants)
        if num_consonants == n:
            result.append(word)
    return result if result else ['None']