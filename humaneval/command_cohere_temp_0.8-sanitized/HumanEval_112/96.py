def reverse_delete(s, c):
    s = list(s)
    c = set(c)
    for char in c:
        s.remove(char)
    s = ''.join(s)
    if s == s[::-1]:
        return s, True
    else:
        return s, False