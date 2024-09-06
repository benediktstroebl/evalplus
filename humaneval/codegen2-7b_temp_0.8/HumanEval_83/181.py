
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if n < 10:
        return 0
    return len(str(10 ** n)) - sum(1 for i in range(1, 10 ** n) if int(i[0])
