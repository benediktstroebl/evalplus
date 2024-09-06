def histogram(test):
    letters = test.strip().lower().replace(" ", "")
    counter = {}
    for letter in letters:
        if letter in counter:
            counter[letter] += 1
        else:
            counter[letter] = 1
    return counter