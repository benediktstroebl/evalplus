
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    def starts_one(n):
        """
        Given a positive integer n, return the count of the numbers of n-digit
        positive integers that start with 1.
        """
        return 9 * 10**(n - 1)

    def ends_one(n):
        """
        Given a positive integer n, return the count of the numbers of n-digit
        positive integers that end with 1.
        """
        # One of the digits in the middle must be 9, because otherwise we'd have
        # two leading 1's and one leading 0.
        return 10**(n - 1) - starts_one(n)

    return starts_one(n) + ends_one(n)

