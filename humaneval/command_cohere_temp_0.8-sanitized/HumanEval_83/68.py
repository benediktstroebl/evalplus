def starts_one_ends(n):
    return sum(str(x)[:n] == '1' or str(x)[:-n] == '1' for x in range(10, 10**n + 10, 2))