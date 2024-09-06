def count_cons(word):
    cons = 0
    for char in word:
        if char != 'a' and char != 'e' and char != 'i' and char != 'o' and char != 'u':
            cons += 1
    return cons
def select_words(s, n):
    words = []
    empty_string = True if s == "" else False
    if empty_string or n <= 0:
        return []

    for word in s.split():
        word = word.strip(".,!?\"'():;")
        if count_cons(word) == n:
            words.append(word)

    return words