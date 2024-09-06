
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if n == 1:
        return 2
    count = 0
    start = 10 ** (n - 2)
    end = 10 ** (n - 1) - 1
    for num in range(start, end + 1):
        if num % 10 == 1 or num // (10 ** (n - 1)) == 1:
            count += 1
    return count
