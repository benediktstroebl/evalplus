
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # n = 2
    if n == 2:
        return 1
    # n > 2
    else:
        # one-end numbers
        count = 0
        for i in range(1, n+1):
            if str(i) == '1':
                count += 1
        return count