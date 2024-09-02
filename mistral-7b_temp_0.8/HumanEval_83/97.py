
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # iterate through the values of n, starting with the first digit
    for i in range(1, n + 1):
        if i == 1:
            return 10 ** (n - 1)
        elif i == 2:
            return 10 ** (n - 2)
        elif i == 3:
            return 10 ** (n - 3)
        else:
            return 10 ** (n - 4)

