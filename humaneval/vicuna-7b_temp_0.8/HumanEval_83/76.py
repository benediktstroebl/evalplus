
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # if n < 10, return 1
    if n < 10:
        return 1

    # base case n == 10
    if n == 10:
        return 2

    # n > 10
    for i in range(1, (n // 10) + 1):
        count = 0
        for j in range(1, n):
            if j // 10 == i - 1:
                count += 1
        count += (n // i) * (n // i + 1) // 2
        return count