
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    result = 0
    for i in range(n):
        result += starts_one_ends_one(i)
    return result
