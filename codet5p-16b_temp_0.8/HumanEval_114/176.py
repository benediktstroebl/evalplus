import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    if len(nums) == 0:
        return math.inf
    if len(nums) == 1:
        return nums[0]
    
    sums = [math.inf] * len(nums)
    sums[0] = nums[0]
    for i in range(1, len(nums)):
        sums[i] = nums[i] + sums[i - 1]
    return min([sums[i] - sums[j] for i in range(len(sums)) for j in range(i, len(sums))])
