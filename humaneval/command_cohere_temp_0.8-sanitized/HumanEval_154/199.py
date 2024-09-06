def cycpattern_check(first, second):
    return second in rotated_substrings(first)
def rotated_substrings(string):
    substrings = [string[i:j] for i in range(len(string)) for j in range(i, len(string))]
    rotated_substrings = [rotated for rotated in substrings if rotated != string and rotated == rotated[::-1]]
    return rotated_substrings