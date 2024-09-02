
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    count = 0

    if n == 1:
        count = 1

    else:
        for i in range(1, n+1):
            if i == 1 or i == n or i == (n-1) or i == (n+1):
                count += 1
            else:
                count += 2

    return count
