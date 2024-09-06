def select_words(s, n):
    words = s.split(' ')
    result = []
    consonants = {"b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"}
    for word in words:
        consonant_count = 0
        for char in word:
            if char in consonants and char != "w":
                consonant_count += 1
        if consonant_count == n:
            result.append(word)
    return result if result else [""]