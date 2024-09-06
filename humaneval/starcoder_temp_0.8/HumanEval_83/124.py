
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    def starts_one(n):
        return 10**(n-1)

    def ends_one(n):
        return 10**n - 1

    return starts_one(n) + ends_one(n) - starts_one(n-1) - ends_one(n-1)

