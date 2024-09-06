def is_happy(s):
    if len(s) < 3:
        return False
    letters_set = set(zip(s[:3], s[1:4], s[2:5]))
    return len(letters_set) == 3