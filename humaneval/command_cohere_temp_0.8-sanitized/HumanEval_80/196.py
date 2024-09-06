def is_happy(s):
    if len(s) < 3:
        return False
    letters_set = set(s[0:3])
    if len(letters_set) == 3 and all(s[i:i+3].count(c) <= 1 for i in range(0, len(s) - 2, 3) for c in letters_set):
        return True
    else:
        return False