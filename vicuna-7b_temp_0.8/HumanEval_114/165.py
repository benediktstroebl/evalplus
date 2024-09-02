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
    else:
        max_sum = nums[-1] + nums[-2]
        for i in range(1, len(nums)):
            min_sum = max_sum + nums[i]
            for j in range(i + 1, len(nums)):
                min_sum -= nums[j]
            if min_sum >= max_sum:
                max_sum = min_sum
        return max_sum
