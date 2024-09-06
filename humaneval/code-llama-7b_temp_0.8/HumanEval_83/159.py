
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if n <= 1:
        return 0
    elif n == 2:
        return 10
    else:
        start = (9, 9, 8, 8, 8, 8, 7, 7, 7, 7, 6)
        end = (1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 4)
        return sum(start[n-3:]) + sum(end[n-3:])

