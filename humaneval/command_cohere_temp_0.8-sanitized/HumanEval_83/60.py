def starts_one_ends(n):
    s = 10 ** n - 9
    e = 10 ** n - 1
    return sum(x == 1 for x in range(s, e, 2))