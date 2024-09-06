def is_happy(s):
    if len(s) < 3:
        return False
    letters_set = set(s[0:3])
    if len(letters_set) < 3:
        return False
    for i in range(3, len(s)):
        if s[i] in letters_set:
            return False
    return True