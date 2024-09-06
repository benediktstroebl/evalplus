def unique_digits(x):
    odd = [y for y in x if not any(int(c) % 2 == 0 for c in str(y))]
    return sorted(odd)