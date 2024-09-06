def count_upper(s):
    c = 0
    for i in range(0, len(s), 2):
        if s[i].isupper() and s[i] in 'AEIOU':
            c += 1
    return c