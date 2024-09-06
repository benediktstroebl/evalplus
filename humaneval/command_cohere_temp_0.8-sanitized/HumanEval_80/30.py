def is_happy(s):
    if len(s) < 3:
        return False
    letters_count = [0, 0, 0]
    for letter in s:
        letters_count[letter] += 1
        if letters_count[letter] == 3:
            letters_count[letter] = 0  # To reset the counter for the next triplet
    return all(count <= 1 for count in letters_count)