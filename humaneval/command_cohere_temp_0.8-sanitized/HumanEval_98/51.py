def count_upper(s):
    upper_vowels = {'A', 'E', 'I', 'O', 'U'}
    count = 0
    for i in range(0, len(s), 2):
        if s[i].isupper() and s[i] in upper_vowels:
            count += 1
    return count