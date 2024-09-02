
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    if n == 1: return 1 # There is only 1 number
    
    count = 0
    for i in range(n):
        if i == 0:
            count += 9 * starts_one_ends(n-1)
        elif i == n-1:
            count += 9
        else:
            count += 9 * starts_one_ends(n-1)
    return count
