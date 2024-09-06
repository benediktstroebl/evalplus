def count_upper(s):
    uppercase_vowels = set(['A', 'E', 'I', 'O', 'U'])
    count = 0
    for i in range(0, len(s), 2):
        if s[i].upper() in uppercase_vowels:
            count += 1
    return count