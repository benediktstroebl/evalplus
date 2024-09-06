def unique_digits(x):
    odd = [int(''.join(c for c in str(i) if c not in '02468')) for i in x if int(''.join(c for c in str(i) if c not in '02468')) == i]
    return sorted(odd)