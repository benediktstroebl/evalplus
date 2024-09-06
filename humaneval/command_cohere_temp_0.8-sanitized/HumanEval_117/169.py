def count_consonants(word):
    cs = 0
    for c in word:
        if c in 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ':
            cs += 1
    return cs
def select_words(s, n):
    words = s.split()
    result = []
    for word in words:
        cc = count_consonants(word)
        if cc == n:
            result.append(word)
    return result