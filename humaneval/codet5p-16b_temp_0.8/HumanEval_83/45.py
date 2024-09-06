
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    if n == 1:
        return 10

    counter = 0
    for i in range(1, 10):
        for j in range(1, 10):
            if str(i).startswith('1') or str(j).endswith('1'):
                counter += 1

    return counter

