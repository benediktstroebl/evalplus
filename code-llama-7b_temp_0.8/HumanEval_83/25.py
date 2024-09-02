
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    count = 0
    # use the first digit as a start/end indicator
    for i in range(10):
        # skip 1, 2, 3, ... and 9 as it does not start with 1
        # skip 10, 11, 12, ... and 19 as it does not end with 1
        if i != 1 and i != 0:
            for j in range(1, n):
                # count every possibility from 10^(n-2) to 9^(n-2)
                count += 9 ** j
    return count
