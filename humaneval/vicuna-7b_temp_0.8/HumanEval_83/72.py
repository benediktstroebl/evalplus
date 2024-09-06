
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if n <= 1:
        return 0
    if n % 10 == 1:
        return (n // 10) * (n // 10) // 2
    else:
        return (n // 10) * (n // 10) // 2 + (n // 10) * (n // 10) // 10
