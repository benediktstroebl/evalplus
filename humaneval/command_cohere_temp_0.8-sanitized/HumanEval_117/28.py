def count_cons(word):
    con = 0
    for char in word:
        if char != 'a' and char != 'e' and char != 'i' and char != 'o' and char != 'u':
            con += 1
    return con
def select_words(s, n):
    words = s.split()
    res = []
    for word in words:
        con = count_cons(word)
        if con == n:
            res.append(word)
    return res if res else ["-"]