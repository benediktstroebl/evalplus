import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    nums = list(nums)
    max_sum = max(sum(nums) for nums in nums)
    for i in range(1, len(nums)):
        curr_sum = sum(nums[:i+1])
        if curr_sum > max_sum:
            continue
        min_sum = curr_sum - max_sum
        for j in range(i+1, len(nums)):
            min_sum -= nums[j]
        return min_sum
    
