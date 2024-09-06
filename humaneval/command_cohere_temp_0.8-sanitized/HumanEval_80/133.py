def is_happy(s):
    if len(s) < 3:
        return False
    letters_occurrences = {}
    for letter in s:
        if letter in letters_occurrences:
            letters_occurrences[letter] += 1
        else:
            letters_occurrences[letter] = 1
    return all(occurrences < 3 for letter, occurrences in letters_occurrences.items())