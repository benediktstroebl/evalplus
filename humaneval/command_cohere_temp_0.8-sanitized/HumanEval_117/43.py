def count_consonants(word):
    counts = {c: 0 for c in 'abcdefghijklmnopqrstuvwxyz'}
    word = word.lower()
    for c in word:
        if c in 'bcdfghjklmnpqrstvwxyz':
            counts[c] += 1
        elif c in 'aeiou':
            counts[''] += -1
        else:
            counts[''] += 1
    return counts[''] <= n
def select_words(s, n):
    words = s.split()
    result = [word for word in words if count_consonants(word) == n]
    return result