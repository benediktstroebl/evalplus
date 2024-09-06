
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    count = 0
    num_digits = 1
    while num_digits < n:
        count += 10 ** (num_digits - 1) * 2
        num_digits += 1
    return count
