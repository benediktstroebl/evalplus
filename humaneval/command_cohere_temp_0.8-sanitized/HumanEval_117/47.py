def count_cons(word):
    cons = 0
    for char in word:
        if char != 'a' and char != 'e' and char != 'i' and char != 'o' and char != 'u':
            cons += 1
    return cons
def select_words(s, n):
    words = s.split()
    res = []
    for word in words:
        if count_cons(word) == n:
            res.append(word)
    return res if res else ['']