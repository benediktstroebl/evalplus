def histogram(test):
    letters = test.strip().lower().replace(" ", "")
    if not letters:
        return {}
    frequency = {}
    for letter in letters:
        if letter in frequency:
            frequency[letter] += 1
        else:
            frequency[letter] = 1
    return frequency