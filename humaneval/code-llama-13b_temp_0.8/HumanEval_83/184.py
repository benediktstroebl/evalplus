
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    n_str = str(n)
    if len(n_str) == 1:
        return 2
    if n_str[0] == '1' or n_str[-1] == '1':
        return starts_one_ends(n - 1) + 1
    else:
        return starts_one_ends(n - 1)
