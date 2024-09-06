def is_happy(s):
    if len(s) < 3:
        return False
    letters_occurrence = {}
    for i in range(len(s)-2):
        first_letter = s[i]
        second_letter = s[i+1]
        third_letter = s[i+2]
        if (first_letter, second_letter, third_letter) in letters_occurrence:
            return False
        letters_occurrence[(first_letter, second_letter, third_letter)] = True
    return True