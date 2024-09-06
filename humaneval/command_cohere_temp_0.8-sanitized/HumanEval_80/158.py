def is_happy(s):
    if len(s) < 3:
        return False
    letters_set = set(s[0:3])
    for i in range(1, len(s) - 2):
        if s[i] in letters_set and s[i + 3] in letters_set:
            return False
        letters_set.add(s[i])
    return True