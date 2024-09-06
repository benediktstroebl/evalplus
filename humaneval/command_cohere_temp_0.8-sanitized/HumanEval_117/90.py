def select_words(s, n):
    words = s.split(' ')
    result = []
    for word in words:
        ct = 0
        for c in word:
            if c != ' ':
                ct += 1
        if ct == n or (n == 0 and ct == 0):
            result.append(word)
    return result