def unique_digits(xs):
    odd = [x for x in xs if any(int(c) % 2 for c in str(x))]
    return sorted(odd)