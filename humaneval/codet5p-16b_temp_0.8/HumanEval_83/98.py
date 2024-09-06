
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    if n <= 0:
        return 0

    digits = [i for i in range(1, n + 1)]
    count = 0
    for digit in digits:
        if digit == 1:
            count += 1

        if digit == n:
            count += 1

        if digit < n:
            count += (10 ** (n - 1) - (digit - 1)) * digit

        if digit > 1:
            count += (10 ** (n - 1) - (digit - 2)) * digit

    return count

