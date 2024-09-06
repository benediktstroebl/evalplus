
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # solution 1
    # start with 1 as the first digit
    count = 0
    for i in range(1, n+1):
        if str(i).startswith(str(n-1)+'1'):
            count += 1
        if str(i).endswith(str(n-1)+'1'):
            count += 1
    return count
