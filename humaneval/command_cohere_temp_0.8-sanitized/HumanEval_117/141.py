def select_words(s, n):
    words = s.split(' ')
    result = []
    for word in words:
        cnt = 0
        for c in word:
            if c != ' ':
                cnt += 1
        if cnt == n:
            result.append(word)
    return result