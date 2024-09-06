import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    max_sum = 0
    for num in nums:
        max_sum = max(max_sum, num)
    for i in range(1, len(nums)):
        j = i
        while j < len(nums):
            if (nums[i] + nums[j]) > max_sum:
                max_sum = nums[i] + nums[j]
                j = min(j + 1, len(nums) - 1)
            else:
                j = j + 1
    return max_sum
