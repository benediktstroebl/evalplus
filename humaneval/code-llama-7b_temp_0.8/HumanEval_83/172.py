
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    starts_one = ends_one = 0

    if n > 1:
        for num_one_digits in range(1, n):
            for num_zero_digits in range(1, n - num_one_digits + 1):
                starts_one += 10**num_zero_digits + 10**(n - num_one_digits) - 1

        for num_zero_digits in range(1, n - 1):
            ends_one += 10**num_zero_digits + 10**(n - num_zero_digits) - 1

        if n == 2:
            ends_one += 10

    elif n == 1:
        starts_one = ends_one = 10

    return starts_one + ends_one
