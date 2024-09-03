def unique_digits(x):
    # Sort list of positive integers without any even digit
    return sorted(x, key=lambda num: (num % 10 != 0))