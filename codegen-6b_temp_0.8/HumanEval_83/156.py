
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    def count_starts_one(n):
        """
        Sub-function for starts_one_ends.
        """
        if n == 1:
            return 1
        elif n == 2:
            return 3
        else:
            return (2 * count_starts_one(n - 1)) + (count_starts_one(n - 2))

    def count_ends_one(n):
        """
        Sub-function for starts_one_ends.
        """
        if n == 1:
            return 2
        elif n == 2:
            return 4
        else:
            return (2 * count_ends_one(n - 1)) + (count_ends_one(n - 2))

    if n == 1:
        return 1
    else:
        return (count_starts_one(n) * 2) + count_ends_one(n)

