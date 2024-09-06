def is_happy(s):
    if len(s) < 3:
        return False
    letters_count = [0, 0, 0]
    for letter in s:
        letters_count[letter] += 1
    for i in range(3):
        if letters_count[i] > 0 and letters_count[i] == letters_count[i-1] == letters_count[i+1]:
            return False
    return True