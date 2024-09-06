def histogram(test):
    letters = test.strip().lower().split()
    count = {}
    for letter in letters:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1
    return count