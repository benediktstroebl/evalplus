
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    count = 0
    for i in range(2, 10 ** n + 1):
        if i > 10 ** (n - 1):
            break
        if i % 10 == 1 or i % 10 == 9:
            count +=
