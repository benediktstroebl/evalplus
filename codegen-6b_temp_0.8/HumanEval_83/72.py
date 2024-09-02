
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if n == 1:
        return 1
    elif n == 2:
        return 0
    elif n == 3:
        return 0
    elif n == 4:
        return 2
    elif n == 5:
        return 1
    elif n == 6:
        return 2
    elif n == 7:
        return 1
    elif n == 8:
        return 4

    # initialize count with 0
    count = 0
    # loop through 1,2,3,...,n-2
    for i in range(1, n - 2):
        s = n - i - 1
        e = n - i
        # count how many numbers start with 1 and end with 1
        count += starts_one_ends(i) * starts_one_ends(s) * starts_one_ends(e)
    return count

