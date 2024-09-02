
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    return sum(1 for num in range(10 ** (n - 1), 10 ** n) if num % 10 == 1 or num % 10 == 0)

