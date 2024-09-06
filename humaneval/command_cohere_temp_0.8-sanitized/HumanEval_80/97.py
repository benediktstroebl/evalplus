def is_happy(s):
    if len(s) < 3:
        return False
    letters_set = set(zip(s[:3], s[1:4], s[2:5]))
    return not any(map(lambda x: len(set(x)) == 1, letters_set))