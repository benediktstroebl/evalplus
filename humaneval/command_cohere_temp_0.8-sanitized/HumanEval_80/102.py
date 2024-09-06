def is_happy(s):
    if len(s) < 3:
        return False
    letters_count = [0] * 256
    for letter in s:
        letters_count[ord(letter)] += 1
    letters_count = [val for val in letters_count if val > 0]
    return len(set(letters_count)) == len(letters_count) == len(s) - 2