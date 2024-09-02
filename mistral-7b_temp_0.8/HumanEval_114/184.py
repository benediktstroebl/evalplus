import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # corner cases
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    min_sum = math.inf
    min_sub_array_len = len(nums)
    for i in range(len(nums)):
        nums_prefix_sum = 0
        nums_suffix_sum = 0
        for j in range(i, len(nums)):
            nums_prefix_sum += nums[j]
            nums_suffix_sum += nums[i - 1 - j]
            sub_array_len = j - i + 2
            if nums_prefix_sum < nums_suffix_sum:
                min_sum = min(min_sum, nums_prefix_sum)
            else:
                min_sum = min(min_sum, nums_suffix_sum)
            min_sub_array_len = min(min_sub_array_len, sub_array_len)
    return min_sum
