
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # count the number of n-digit numbers that end with 1
    count = 0
    for i in range(1, n+1):
        if int(str(i))[-1] == 1:
            count += 1
    return count
