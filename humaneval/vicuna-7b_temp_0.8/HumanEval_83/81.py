
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # Add the count of single digits 1
    return 1 + (n//100 * (n//100 // 10) + (n//10 % 10))
