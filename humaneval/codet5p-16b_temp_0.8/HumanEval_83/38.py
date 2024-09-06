
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    count = 0
    for i in range(n):
        if i == 0 or i == n-1:
            count += 2
        else:
            count += 1
    return count


