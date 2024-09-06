def unique_digits(x):
    odd = [int(''.join(c for c in str(n) if c not in '02468')) for n in x if n % 2]
    return sorted(odd)