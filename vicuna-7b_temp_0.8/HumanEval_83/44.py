
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # base cases
    if n == 1:
        return 1
    if n == 2:
        return 1
    # recurrence case
    return (n//10-1)*starts_one_ends(n//10) + starts_one_ends(n%10)

