
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if n == 1:
        return 2

    count = 0
    for i in range(1, 10):
        if i == 1 or i == 9:
            count += 1
        else:
            count += 2

    return count
