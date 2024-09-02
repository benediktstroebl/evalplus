
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if n == 1:
        return 6
    if n == 2:
        return 10
    if n == 3:
        return 10
    def helper(n, one_count):
        if n == 1:
            one_count *= 4
        elif n == 2:
            one_count *= 12
        elif n == 3:
            one_count *= 22
        else:
            one_count *= 30
        return one_count
    return 6 + helper(n-1, 10) + helper(n-2, 10) + helper(n-3, 10)
