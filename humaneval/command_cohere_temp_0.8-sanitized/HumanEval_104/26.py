def unique_digits(x):
    odd = [int(''.join(c for c in str(i) if c % 2 != 0)) for i in x if int(''.join(c for c in str(i) if c % 2 != 0)) <= len(str(x)) ]
    return sorted(odd)