
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    count = 0
    for i in range(1, n):
        if n%2 == 1:
            count += 2
        else:
            count += 4
    return count
