
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # n-1 because n-1 digits are left after the first one
    digits = 10 ** n - 1
    starts = 0
    ends = 0
    for i in range(1, digits+1):
        if i % 2 == 0:
            starts += 1
        else:
            ends += 1
    return starts + ends
