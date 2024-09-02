
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if n < 2:
        return 0
    n_digit = 10 ** (n - 1)
    starts = 0
    ends = 0
    while n_digit < 10 ** n:
        starts += n_digit // 10
        ends += 10 ** n // 10 - 1
        n_digit *= 10
    return starts + ends

