
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    num_digits = len(str(n))
    ones = str(1) * num_digits
    return count_in_range(ones + "0", "9" * num_digits) + count_in_range(ones, ones)

