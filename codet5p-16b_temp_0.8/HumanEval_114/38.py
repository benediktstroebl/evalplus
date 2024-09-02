import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    def sum_helper(sub):
        return sum(sub)
    nums_len = len(nums)
    if nums_len == 0:
        return math.inf
    if nums_len == 1:
        return nums[0]
    sub_lens = range(1, nums_len + 1)
    sub_min_sum = math.inf
    for sub_len in sub_lens:
        for i in range(nums_len - sub_len + 1):
            sub = nums[i:i + sub_len]
            sub_sum = sum_helper(sub)
            if sub_sum < sub_min_sum:
                sub_min_sum = sub_sum
    return sub_min_sum
