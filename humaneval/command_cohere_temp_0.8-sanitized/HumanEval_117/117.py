def count_consonants(word):
    ct = 0
    for c in word:
        if c in 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ':
            ct += 1
    return ct
def select_words(s, n):
    words = [w for w in s.split(' ') if w]
    return [w for w in words if count_consonants(w) == n]