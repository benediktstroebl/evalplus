def starts_one_ends(n):
    counts = [0, 0, 1, 0, 0, 0, 1, 2, 1, 0, 1, 0, 0, 1, 1, 1, 2, 1, 0, 1, 1, 1, 1, 2, 1, 2, 1, 1, 1]
    if n > 10:
        return counts[n - 11]
    else:
        return counts[n]