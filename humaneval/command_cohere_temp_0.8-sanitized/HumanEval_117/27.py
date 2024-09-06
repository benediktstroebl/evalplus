def count_consonants(word):
    cnt = 0
    for char in word:
        if char.isalpha():
            if char in 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ':
                cnt += 1
    return cnt
def select_words(s, n):
    words = []
    word = ""
    for c in s:
        if c == ' ':
            if count_consonants(word) == n:
                words.append(word)
            word = ""
        else:
            word += c
    if count_consonants(word) == n:
        words.append(word)
    return words