def count_consonants(word):
    consonants = 0
    for char in word:
        if char != "a" and char != "e" and char != "i" and char != "o" and char != "u" and char.isalpha():
            consonants += 1
    return consonants
def select_words(s, n):
    words = s.split()
    result = []
    for word in words:
        consonant_count = count_consonants(word)
        if consonant_count == n:
            result.append(word)
    return result