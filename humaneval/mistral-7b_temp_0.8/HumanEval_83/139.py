
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    count = 0
    if (n == 1):
        return 1
    elif (n > 1):
        while (n > 0):
            n -= 1
            if (n == 0):
                count += 1
            else:
                count += 2
        return count

