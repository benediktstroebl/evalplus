def unique_digits(x):
    odd = [int(''.join(c for c in s if c % 2 != 0)) for s in x]
    return sorted(odd)