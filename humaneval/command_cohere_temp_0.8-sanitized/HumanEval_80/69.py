def is_happy(s):
    if len(s) < 3:
        return False
    letters_count = [0, 0, 0]
    for letter in s:
        letters_count[letter] += 1
    return all(count < 3 for count in letters_count)