def select_words(s, n):
    words = s.split(' ')
    result = []
    for word in words:
        cnt = 0
        for char in word:
            if char.isalpha():
                if char.lower() != char.upper():
                    cnt += 1
        if cnt == n:
            result.append(word)
    return result