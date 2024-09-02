
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # count of 1-digit numbers
    one_count = 1
    # count of 2-digit numbers
    two_count = 1
    # ...
    # count of n-digit numbers
    n_count = 1
    # if n is 1, return 1
    if n == 1:
        return 1
    # for the rest of the cases
    for i in range(2, n+1):
        # increment the count of n-digit numbers
        n_count *= i
        # for the first digit
        if n % i == 0:
            # increment the count of 1-digit numbers
            one_count *= i
        # for the last digit
        if n % i == i-1:
            # increment the count of 1-digit numbers
            one_count *= i
        # for the middle digits
        for j in range(2, n//i):
            # increment the count of n-digit numbers
            n_count *= j
            # increment the count of 1-digit numbers
            one_count *= j
    return n_count + one_count
