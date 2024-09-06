def starts_one_ends(n):
    counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    if n >= 1:
        counts[0] = 1
    if n >= 2:
        counts[1] = 10
    for i in range(2, n):
        if i % 2 == 1:
            counts[i] = 9 * 10 ** (n - i - 1)
        else:
            counts[i] = 10 ** (n - i - 1) - 9 * 10 ** (n - i - 1)
    return counts[n]