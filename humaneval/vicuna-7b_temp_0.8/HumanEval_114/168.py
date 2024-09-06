import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    max_len = max(len(x) for x in nums)
    min_sum = max_len * 2 + 1
    for i in range(1, len(nums)):
        for j in range(i):
            for k in range(i+1, len(nums)):
                if nums[i] + nums[j] + nums[k] < nums[i] or nums[i] + nums[j] + nums[k] < nums[k]:
                    min_sum = min(min_sum, nums[i] + nums[j] + nums[k])
    return min_sum

nums = [1,2,3,4,5]
