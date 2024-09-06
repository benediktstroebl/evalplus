def select_words(s, n):
    words = s.split(' ')
    result = []
    for word in words:
        consonantCount = 0
        for char in word:
            if char.isalpha():
                if char.lower() != char.upper():
                    consonantCount += 1
        if consonantCount == n:
            result.append(word)
    return result if result else ['None']