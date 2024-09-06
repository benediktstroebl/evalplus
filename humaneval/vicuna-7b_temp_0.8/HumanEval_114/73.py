import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # find the length of the array
    n = len(nums)
    # initialize the sum of the sub-array to the sum of the entire array
    sum = nums[0]
    for i in range(1, n):
        sum += nums[i]
    # initialize the starting point of the sub-array
    start = 0
    # initialize the ending point of the sub-array
    end = start
    while end < n:
        # if the end point is greater than the length of the array
        # then we have found a sub-array with a sum less than or equal to 0
        if end >= n:
            return -1
        # if the sub-array is not empty
        if nums[start] > 0:
            # subtract the sum of the sub-array from the sum of the entire array
            sum -= nums[start]
            # update the starting point
            start += 1
            # update the ending point
            end = start
        # if the start point is greater than the length of the array
        # then we have found a sub-array with a sum greater than the entire array
        if start >= n:
            return -1
        # update the ending point
        end = start
        # update the starting point
        start = 0
    return -1
