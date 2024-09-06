def select_words(s, n):
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    words = s.split(' ')
    result = []

    for word in words:
        cnt = sum(1 for char in word if char in consonants)
        if cnt == n:
            result.append(word)

    return result if result else []