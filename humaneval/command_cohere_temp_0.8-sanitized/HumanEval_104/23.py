def unique_digits(xs):
    res = [x for x in xs if not any(int(y) % 2 == 0 for y in str(x))]
    return sorted(res)