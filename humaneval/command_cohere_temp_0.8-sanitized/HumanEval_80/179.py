def is_happy(s):
    if len(s) < 3:
        return False
    letters_set = set(s)
    return len(s) % 3 == 0 and len(letters_set) == len(s) - 2