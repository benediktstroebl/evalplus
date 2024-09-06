def count_consonants(word):
    counts = 0
    for char in word:
        if char.isalpha():
            if char.lower() != 'a' and char.lower() != 'e' and char.lower() != 'i' and char.lower() != 'o' and char.lower() != 'u':
                counts += 1
    return counts
def select_words(s, n):
    words = s.split()
    result = []
    for word in words:
        consonant_count = count_consonants(word)
        if consonant_count == n:
            result.append(word)
    return result