def is_happy(s):
    if len(s) < 3:
        return False
    letters_occurrence = [0] * 256  # Assuming ASCII
    for letter in s:
        letters_occurrence[ord(letter)] += 1
    return all(occurrence < 3 for occurrence in letters_occurrence)