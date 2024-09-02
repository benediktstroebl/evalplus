
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    # For example, if n = 1, then the count should be 2 because there are 2
    # one-digit numbers that start or end with 1: 1 and 11.
    # If n = 2, then the count should be 3 because there are 3 two-digit
    # numbers that start or end with 1: 11, 13, and 19.

    # One could brute force the solution, but that would be pretty slow.
    # Is there a more efficient solution?

    count = 0

    # Because there is no one-digit number with a 1 in the middle,
    # all the one-digit numbers that start or end with 1
    # are in the range 0 through 9.
    for i in range(10):
        if i == 1:
            count += 2
            continue
        if str(i) in "11":
            count += 2

    # Can we do better than this brute-force approach?
    for i in range(10, n * 10):
        for j in range(10):
            if str(j) in "11":
                count += 1
    return count
