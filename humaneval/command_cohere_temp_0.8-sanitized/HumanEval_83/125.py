def starts_one_ends(n):
    return sum(int(x) >= 1 for x in itertools.product('01', repeat=n))