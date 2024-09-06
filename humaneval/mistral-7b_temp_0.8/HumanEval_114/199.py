import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # iterate through the nums
    # if the sum is less than current, update
    # return current sum
    minSum = nums[0]
    currSum = nums[0]
    for num in nums[1:]:
        if currSum < 0:
            currSum = num
        else:
            currSum += num
        if currSum < minSum:
            minSum = currSum
    return minSum
