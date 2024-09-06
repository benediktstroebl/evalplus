def starts_one_ends(n):
    counts = [0 for i in range(n)]
    counts[0] = 1

    # Count numbers starting with 1
    for i in range(1, n):
        if i >= 10:
            counts[i] += counts[i-10]
        else:
            counts[i] += 1

    # Count numbers ending with 1
    for i in range(1, n):
        if i <= 9:
            counts[i] += counts[n-1-i]
        else:
            counts[i] += 1

    return sums(counts)
def sums(iterable):
    res = 0
    for i in iterable:
        res += i
    return res