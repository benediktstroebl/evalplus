def count_consonants(word):
    count = 0
    for char in word:
        if char.isalpha():
            if char.lower() != 'a' and char.lower() != 'e' and char.lower() != 'i' and char.lower() != 'o' and char.lower() != 'u':
                count += 1
    return count
def select_words(s, n):
    words = s.split()
    result = []
    for word in words:
        if count_consonants(word) == n:
            result.append(word)
    return result