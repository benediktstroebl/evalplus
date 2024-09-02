
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    return sum(len([x for x in range(10 ** (n - 1), 10 ** n) if
                    x[0] == "1" or x[-1] == "1"]) for n in range(1, 9))
