
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    def helper(num, i):
        if i == 0:
            return 1
        elif num % 10 == 1:
            return 2 * helper(num, i - 1)
        else:
            return helper(num, i - 1)
    if n == 1:
        return 1
    else:
        return 2 * helper(n, n - 1)

