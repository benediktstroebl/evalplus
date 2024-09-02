import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # Variables
    numLen = len(nums)
    sum = 0
    minSum = float('inf')
    i = 0
    j = 0
    # while loop fins the lowest sum
    while j < numLen:
        # add the next elemnt
        sum += nums[j]
        if sum < minSum:
            minSum = sum
        # if the sum is bigger than the last element,
        #  the new sum is the last elemnt
        if sum > nums[j]:
            sum = nums[j]
        j += 1
    return minSum
