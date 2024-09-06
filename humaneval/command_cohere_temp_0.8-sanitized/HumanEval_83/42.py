def starts_one_ends(n):
    # Create a list to store the counts of starting or ending with 1
    counts = [0] * n

    # Count numbers that start with 1
    for i in range(1, 10 * n, 10):
        counts[i % n] += 1

    # Count numbers that end with 1
    for i in range(9 * n, 0, -10):
        counts[i % n] += 1

    return sumsolve(counts)
def sumsolve(seq):
    # Calculate the sum required to solve the problem
    if len(seq) == 1:
        return seq[0]
    else:
        return sum(seq[:len(seq) // 2]) + sum(seq[len(seq) // 2:])