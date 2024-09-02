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
    if len(nums) == 1:
        return nums[0]
    sums = [0]*len(nums)
    sums[0] = nums[0]
    sums[1] = max(nums[0], nums[1])
    for i in range(2, len(nums)):
        sums[i] = max(sums[i-1] + nums[i], nums[i])
    print sums
    return max(sums)

