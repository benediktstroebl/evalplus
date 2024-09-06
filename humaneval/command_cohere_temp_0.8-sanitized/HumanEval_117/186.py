def count_consonants(word):
    ct = 0
    for char in word:
        if char != 'a' and char != 'e' and char != 'i' and char != 'o' and char != 'u':
            ct += 1
    return ct
def select_words(s, n):
    words = s.split()
    result = []
    for word in words:
        ct = count_consonants(word)
        if ct == n:
            result.append(word)
    return result