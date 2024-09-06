
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    def starts_with_one(n):
        # base case
        if n <= 0:
            return 0
        elif n == 1:
            return 10
        elif n == 2:
            return 8

        return starts_with_one(n - 1) + starts_with_one(n - 2)

    def ends_with_one(n):
        # base case
        if n <= 0:
            return 0
        elif n == 1:
            return 10
        elif n == 2:
            return 7

        return ends_with_one(n - 1) + ends_with_one(n - 2)

    return starts_with_one(n - 1) + ends_with_one(n - 1)
