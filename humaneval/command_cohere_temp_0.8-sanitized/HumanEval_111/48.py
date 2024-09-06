def histogram(test):
    letters = test.split()
    letters = [letter for letter in letters if letter.isalpha() and letter.lower() in letter]
    if len(letters) == 0:
        return {}
    count_letter = {}
    for letter in letters:
        if letter in count_letter:
            count_letter[letter] += 1
        else:
            count_letter[letter] = 1
    return count_letter