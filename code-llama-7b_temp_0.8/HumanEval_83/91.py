
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    num = n
    count = 0

    # There are 10^(n-1) numbers that start with 1
    count += 10 ** (num-1)

    # There are 10^(n-2) numbers that end with 1
    count += 10 ** (num-2)

    # Return the result
    return count

