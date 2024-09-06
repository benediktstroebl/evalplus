def histogram(test):
    letters = test.lower().strip().split()
    dictionary = {}
    for letter in letters:
        if letter in dictionary:
            dictionary[letter] += 1
        else:
            dictionary[letter] = 1
    return dictionary