def is_happy(s):
    if len(s) < 3:
        return False
    letters_count = [0] * 256  # Assuming ASCII
    for letter in s:
        letters_count[ord(letter)] += 1
    return all(count % 3 == 0 and count > 0 for count in letters_count[::3])