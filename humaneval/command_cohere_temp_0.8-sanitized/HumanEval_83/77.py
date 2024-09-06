def starts_one_ends(n):
    return sum(int(s) == 1 for s in itertools.product('0123456789', repeat=n))