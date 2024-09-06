def count_consonants(word):
    cs = 0
    for c in word:
        if c in 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ':
            cs += 1
    return cs
def select_words(s, n):
    words = []
    s += ' '
    for word in s.split():
        if count_consonants(word) == n:
            words.append(word)
    return words