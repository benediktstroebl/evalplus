import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # case handling
    if nums == None:
        return None
    if len(nums) == 0:
        return None

    # actual code
    minSum, sum, start = math.inf, 0, 0
    for end in range(len(nums)):
        sum += nums[end]
        if sum < minSum:
            minSum = sum
            start = end
        elif sum >= minSum:
            sum = 0
            start = end + 1

    return minSum

