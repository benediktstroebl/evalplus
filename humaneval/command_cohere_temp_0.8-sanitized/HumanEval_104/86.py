def unique_digits(xs):
    odd_digits = [int(''.join(x for x in str(n) if x.isdigit() and x % 2 != 0)) for n in xs if n > 0]
    return sorted(odd_digits)