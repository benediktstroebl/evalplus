def reverse_delete(s, c):
    s = ''.join(x for x in s if x not in c)
    return s, s == s[::-1]