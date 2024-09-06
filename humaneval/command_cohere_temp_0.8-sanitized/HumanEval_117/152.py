def count_consonants(word):
    ct = 0
    for c in word:
        if c in 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ':
            ct += 1
    return ct
def select_words(s, n):
    words = s.split()
    res = []
    for w in words:
        if count_consonants(w) == n:
            res.append(w)
    return res if res else ['']