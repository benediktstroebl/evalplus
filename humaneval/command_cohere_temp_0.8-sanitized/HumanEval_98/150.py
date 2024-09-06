def count_upper(s):
    ct = 0
    for i in range(0, len(s), 2):
        if s[i].isupper() and s[i].lower() in 'AEIOU':
            ct += 1
    return ct