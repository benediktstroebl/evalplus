def count_cons(word):
    con = 0
    for char in word:
        if char != 'a' and char != 'e' and char != 'i' and char != 'o' and char != 'u':
            con += 1
    return con
def select_words(s, n):
    words = []
    empty_string = True if s == "" else False
    if empty_string or n <= 0:
        return []
    for word in s.split():
        con = count_cons(word)
        if con == n:
            words.append(word)  
    return words