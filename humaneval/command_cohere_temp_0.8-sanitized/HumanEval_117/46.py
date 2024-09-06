def count_cons(word):
    ct = 0
    for char in word:
        if char != 'a' and char != 'e' and char != 'i' and char != 'o' and char != 'u':
            ct += 1
    return ct
def select_words(s, n):
    words = []
    for w in s.split():
        ct = count_cons(w)
        if ct == n:
            words.append(w)
    return words