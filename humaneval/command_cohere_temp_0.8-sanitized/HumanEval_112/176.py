def reverse_delete(s, c):
    delete = [char for char in c]
    reversed_s = s[:0]
    for i, char in enumerate(s):
        if char not in delete:
            reversed_s = reversed_s + char
    return reversed_s, reversed_s == s