def is_happy(s):
    if len(s) < 3:
        return False
    letters_dict = {}
    letters_count = 0
    for letter in s:
        if letter in letters_dict:
            letters_dict[letter] += 1
        else:
            letters_dict[letter] = 1
            letters_count += 1
        if letters_count == 3:
            letters_count = 0
    return len(letters_dict) == len(s)