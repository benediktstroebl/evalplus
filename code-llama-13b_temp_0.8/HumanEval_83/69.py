
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # NOTE: if the leading digit is 0, it doesn't start with 1
    if n == 1:
        return 1  # 10, 11, 12, ...
    # 100 = 1*100 is the first n-digit number starting with 1
    return (10 ** (n - 1)) * 2
