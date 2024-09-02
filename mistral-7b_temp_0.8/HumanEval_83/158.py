
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    count = 0
    if n == 1:
        return 2
    elif n > 1:
        if n % 2 == 1:
            count += 10 ** (n - 2) + 10 ** (n - 1) + 10 ** n
        else:
            count += 10 ** (n - 1) + 10 ** n
        count += starts_one_ends(n - 1)
        return count
    return 0
