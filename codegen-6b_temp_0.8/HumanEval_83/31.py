
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    nums = [0]*(n+1)
    nums[0] = 1
    nums[1] = 10
    nums[2] = 25
    for i in xrange(3,n+1):
        nums[i] = (nums[i-1]*9 + nums[i-2]*9)
    return nums[n]//9
