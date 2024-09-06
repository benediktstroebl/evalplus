def count_cons(word):
    cnt = 0
    for char in word:
        if char != 'a' and char != 'e' and char != 'i' and char != 'o' and char != 'u':
            cnt += 1
    return cnt
def select_words(s, n):
    words = s.split()
    res = []
    for word in words:
        cnt = count_cons(word)
        if cnt == n:
            res.append(word)
    return res if res != [] else res