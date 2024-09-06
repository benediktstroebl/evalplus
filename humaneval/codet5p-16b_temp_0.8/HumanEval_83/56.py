
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    def ends_with(n):
        if n == 1:
            return 1
        else:
            return 10*ends_with(n-1)
    def starts_with(n):
        if n == 1:
            return 1
        else:
            return 9*starts_with(n-1)+ends_with(n-1)
    return starts_with(n)+ends_with(n)
