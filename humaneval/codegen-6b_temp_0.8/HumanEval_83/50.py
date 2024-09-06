
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    count = 0
    for x in xrange(1, 10**n):
        nums = str(x)
        if nums[0] == '1':
            count += 1
        if nums[-1] == '1':
            count += 1
    return count
