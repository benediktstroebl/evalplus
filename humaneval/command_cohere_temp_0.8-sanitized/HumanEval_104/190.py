def unique_digits(x):
    odd = [int(''.join(c for c in str(n) if c % 2 != 0)) for n in x if int(''.join(c for c in str(n) if c % 2 != 0)) <= n]
    return sorted(odd)