def count_consonants(word):
    cnt = 0
    for char in word:
        if char.lower() in 'bcdfghjklmnpqrstvwxyz':
            cnt += 1
    return cnt
def select_words(s, n):
    words = s.split()
    result = []
    for word in words:
        cnt = count_consonants(word)
        if cnt == n:
            result.append(word)
    return result