
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    return sum(n >= int(str(x)[0] == "1" or str(x)[-1] == "1")
               for x in range(1, n + 1))
