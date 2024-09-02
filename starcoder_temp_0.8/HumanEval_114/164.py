import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    if not nums:
        return 0
    for i in range(len(nums)):
        nums[i] *= -1
    prefixSums = nums[:]
    # print(prefixSums)
    for i in range(1, len(prefixSums)):
        prefixSums[i] = max(prefixSums[i - 1] + nums[i], 0)
    # print(prefixSums)
    return max(prefixSums)
