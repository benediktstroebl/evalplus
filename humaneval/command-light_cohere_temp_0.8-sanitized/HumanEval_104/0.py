def unique_digits(x):
    # Sort list of positive integers without any even digit
    return sorted([i for i in x if i % 10 != 0])