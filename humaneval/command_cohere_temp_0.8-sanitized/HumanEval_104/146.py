def unique_digits(x):
    odd = [int for int in x if int % 2 != 0]
    return sorted(odd)