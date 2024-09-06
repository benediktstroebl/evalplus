def unique_digits(xs):
    odd = [x for x in xs if any(int(y) % 2 for y in str(x))]
    return sorted(odd)