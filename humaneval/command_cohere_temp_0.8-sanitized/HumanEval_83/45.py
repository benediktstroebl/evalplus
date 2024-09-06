def starts_one_ends(n):
    return sum(map(lambda x: 1 if x[0] == '1' or x[-1] == '1' else 0,
                      itertools.combinations(range(10**n), n)))