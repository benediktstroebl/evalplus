def is_happy(s):
    if len(s) < 3:
        return False
    letters_set = set(s[0:3])
    for i in range(1, len(s) - 2):
        if len(letters_set) != len(set(s[i:i+3])):
            return False
    return True