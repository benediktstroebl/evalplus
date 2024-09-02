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

    sums = [nums[0]]
    for i in range(1, len(nums)):
        sums.append(sums[-1] + nums[i])

    return min(sums[i + 1] - sums[i] for i in range(len(sums) - 1))

