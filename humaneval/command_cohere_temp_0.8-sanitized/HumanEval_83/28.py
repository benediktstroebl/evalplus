def starts_one_ends(n):
    counts = [0 for i in range(n + 1)]
    counts[1] = 1

    for i in range(2, n + 1):
        if i % 2 == 1:
            counts[i] = counts[i - 1]
        else:
            counts[i] = counts[i - 2]
    return counts[-1]