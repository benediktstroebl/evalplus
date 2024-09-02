
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    starts_1 = sum([starts_1_helper(str(n)) for n in range(1, n + 1)])
    ends_1 = sum([ends_1_helper(str(n)) for n in range(1, n + 1)])
    return starts_1 + ends_1
