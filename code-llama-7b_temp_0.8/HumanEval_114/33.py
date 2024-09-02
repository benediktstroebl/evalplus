import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    nums_sum = sum(nums)
    nums_len = len(nums)
    if nums_len == 1:
        return nums_sum
    min_sum = math.inf
    i = 0
    while i < nums_len:
        j = i+1
        while j <= nums_len:
            sum_cur = sum(nums[i:j])
            if sum_cur < min_sum:
                min_sum = sum_cur
            j += 1
        i += 1
    return min_sum
