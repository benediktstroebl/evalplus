def count_cons(word):
    cnt = 0
    for char in word:
        if char != 'a' and char != 'e' and char != 'i' and char != 'o' and char != 'u':
            cnt += 1
    return cnt
def select_words(s, n):
    words = []
    word = ""
    for c in s:
        if c == ' ':
            if count_cons(word) == n:
                words.append(word)
            word = ""
        else:
            word += c
    if count_cons(word) == n:
        words.append(word)
    return words