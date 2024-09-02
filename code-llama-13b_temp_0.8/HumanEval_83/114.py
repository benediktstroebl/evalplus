
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    # count of all n-digit numbers
    count = pow(10, n)

    # count of all n-digit numbers that start with 1
    start_1_count = pow(10, n-1)

    # count of all n-digit numbers that end with 1
    end_1_count = pow(10, n-1)

    return count - start_1_count - end_1_count + 1

