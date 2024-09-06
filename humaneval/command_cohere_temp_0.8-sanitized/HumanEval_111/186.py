def histogram(test):
    letters = test.split()
    histogram = {}
    for letter in letters:
        if letter in histogram:
            histogram[letter] += 1
        else:
            histogram[letter] = 1
    return histogram