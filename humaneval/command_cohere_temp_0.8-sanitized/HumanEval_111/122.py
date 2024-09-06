def histogram(test):
    letters = test.strip().lower().replace(' ', '')
    if not letters:
        return {}
    dictLetters = {}
    for letter in letters:
        if letter in dictLetters:
            dictLetters[letter] += 1
        else:
            dictLetters[letter] = 1
    return dictLetters