def count_consonants(word):
    cnt = 0
    for char in word:
        if char != 'a' and char != 'e' and char != 'i' and char != 'o' and char != 'u' and \
           char != 'y' and char != 'A' and char != 'E' and char != 'I' and char != 'O' and char != 'U' and \
           char != 'Y':
            cnt += 1
    return cnt
def select_words(s, n):
    words = s.split()
    result = []
    for word in words:
        if count_consonants(word) == n:
            result.append(word)
    return result