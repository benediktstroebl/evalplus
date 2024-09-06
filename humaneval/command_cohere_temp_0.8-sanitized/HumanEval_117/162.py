def count_cons(word):
    con = 0
    for char in word:
        if char != 'a' and char != 'e' and char != 'i' and char != 'o' and char != 'u':
            con += 1
    return con
def select_words(s, n):
    words = []
    str_list = s.split()
    for word in str_list:
        con = count_cons(word)
        if con == n:
            words.append(word)
    return words