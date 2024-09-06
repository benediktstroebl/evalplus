def starts_one_ends(n):
    counts = [0, 0, 1, 0, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 0]
    if n <= 10:
        return counts[n-1]
    else:
        return counts[10] + starts_one_ends(n-1)