def is_happy(s):
    if len(s) < 3:
        return False
    letters_occurrence = [0] * len(s)
    for i in range(len(s)):
        letters_occurrence[i] = s[i]
    for i in range(len(s) - 2):
        if letters_occurrence[i] == letters_occurrence[i + 2]:
            return False
    return True