def is_happy(s):
    if len(s) < 3:
        return False
    letters_count = [0] * 128
    letters_set = set()
    letters_set_size = 0
    for letter in s:
        letters_count[ord(letter)] += 1
        letters_set.add(letter)
        letters_set_size += 1
        if letters_set_size == 3:
            if len(letters_set) == 1:
                return False
            else:
                letters_set.clear()
                letters_set_size = 0
    return True