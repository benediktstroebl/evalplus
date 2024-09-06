
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    return sum(len(str(x)) == n and (str(x)[0] == "1" or str(x)[-1] == "1") for x in range(10 ** (n - 1), 10 ** n))

