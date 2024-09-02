
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if n == 1:
        return 1

    starts_ones = 1  # because 11..
    ends_ones = 1  # because ..11

    for i in range(2, n):
        starts_ones += 10**(i - 1)
        ends_ones += 10**(i - 1)

    return starts_ones + ends_ones
