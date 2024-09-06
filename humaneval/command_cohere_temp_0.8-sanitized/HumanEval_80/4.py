def is_happy(s):
    if len(s) < 3:
        return False
    letters_count = [0] * 256
    for letter in s:
        letters_count[ord(letter)] += 1
    letters_count[0] -= 1  # one of the letters should be counted twice
    return all(count % 3 == 0 and count != 0 for count in letters_count[1:])