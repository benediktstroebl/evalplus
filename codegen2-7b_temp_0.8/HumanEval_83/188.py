
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    return sum(1 if n % 10 == 1 else 0 for n in range(1, int(n/10)+1)
