import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    """
    n = len(nums)
    sub = sum(nums)

    if sub == 0:
        return sub

    if sub < 0:
        return -1

    # keep track of the minimum sum of a subarray
    minsum = [0] * n
    minsum[0] = nums[0]
    for i in range(1, n):
        minsum[i] = min(minsum[i-1] + nums[i], nums[i])

    return min(minsum)
    """
    n = len(nums)
    sub = sum(nums)
    if sub == 0:
        return sub

    if sub < 0:
        return -1

    currmin = nums[0]
    currsum = 0
    for i in range(n):
        currsum += nums[i]

        # check if we have a new min
        if currsum < 0:
            currsum = 0

        if currsum < currmin:
            currmin = currsum

    return currmin

