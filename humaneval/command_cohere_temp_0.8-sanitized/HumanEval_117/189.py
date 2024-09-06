def count_consonants(word):
    ct = 0
    for char in word:
        if char != 'a' and char != 'e' and char != 'i' and char != 'o' and char != 'u' and \
           char != 'A' and char != 'E' and char != 'I' and char != 'O' and char != 'U' and \
           char != 'y' and char != 'Y':
            ct += 1
    return ct
def select_words(s, n):
    words = s.split()
    res = []
    for w in words:
        ct = count_consonants(w)
        if ct == n:
            res.append(w)
    return res