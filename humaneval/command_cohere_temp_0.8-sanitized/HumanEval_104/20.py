def unique_digits(xs):
    odd_digits = [int(''.join(x for x in str(n) if x.isdigit() and x % 2 != 0)) for n in xs]
    return sorted(odd_digits)