import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    max_sum = max(sum(nums) for nums in product(nums, repeat=2))
    result = {}
    for i, num in enumerate(nums):
        if len(set(nums[:i+1])) == len(nums):
            sub_sum = sum(nums[:i+1])
            if sub_sum < max_sum - i:
                max_sum = sub_sum
                min_i = i
    return min_i
