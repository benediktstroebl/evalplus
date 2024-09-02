
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    total = 0
    for i in range(n):
        count = 0
        for j in range(i+1, n):
            if (j // 10 == i % 10) or (j % 10 == i // 10):
                count += 1
        total += count
    return total
