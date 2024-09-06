
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if n <= 0:
        return 0
    elif n <= 1:
        return 1
    else:
        first_numbers = 10**(n-1)
        last_numbers = 10**(n-1)
        return first_numbers + last_numbers + starts_one_ends(n-1)

