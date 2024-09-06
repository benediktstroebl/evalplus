def count_cons(word):
    ct = 0
    for char in word:
        if char != 'a' and char != 'e' and char != 'i' and char != 'o' and char != 'u':
            ct += 1
    return ct
def select_words(s, n):
    words = []
    str_list = s.split()
    for word in str_list:
        ct = count_cons(word)
        if ct == n:
            words.append(word)
    return words