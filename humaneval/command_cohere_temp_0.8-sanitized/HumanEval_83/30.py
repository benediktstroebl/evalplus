def starts_one_ends(n):
    counts = [0 for i in range(10)]
    for i in range(10, 10**n + 1):
        if i % 10 == 1:
            counts[i % 10] += 1
    return counts[1] + counts[9]