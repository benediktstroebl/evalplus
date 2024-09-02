
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    start = 10 ** (n - 1)
    end = 10 ** n
    one_starts = 10 ** (n - 1)
    one_ends = 10 ** (n - 1) + 9
    return sum(i >= start and i <= end and i >= one_starts and i <= one_ends
               for i in range(1, 10 ** n + 1))
