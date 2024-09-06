def pairs_sum_to_zero(l):
    # iterate through all pairs
    for x, y in combinations(l, 2):
        if x + y == 0:
            return True
    return False