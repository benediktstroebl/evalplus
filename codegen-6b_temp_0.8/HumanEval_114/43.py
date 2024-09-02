import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # The minimum subarray sum is the minimum of the following:
    # 1) The minimum subarray sum of any prefix
    # 2) The minimum subarray sum of any suffix
    # 3) The minimum subarray sum of the entire array
    # The maximum of these is the total sum of the array

    prefix_sum = 0
    prefix_sums = [0 for i in range(len(nums))]
    suffix_sums = [0 for i in range(len(nums))]
    for i in range(len(nums)):
        prefix_sum = min(prefix_sum + nums[i], nums[i])
        prefix_sums[i] = prefix_sum
    min_sum = float("inf")
    for i in range(len(nums)):
        if i == 0:
            min_sum = min(min_sum, prefix_sums[i])
        else:
            min_sum = min(min_sum, prefix_sums[i] - suffix_sums[i - 1])
        suffix_sums[len(nums) - i - 1] = prefix_sums[len(nums) - 1 - i]
    return min_sum

