import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    nums_len = len(nums)

    if nums_len == 1:
        return nums[0]

    nums_sum = sum(nums)
    min_sub_array_sum = nums_sum

    for i in range(nums_len):
        for j in range(i, nums_len):
            sub_array = nums[i:j + 1]
            sub_array_sum = sum(sub_array)

            if sub_array_sum < min_sub_array_sum:
                min_sub_array_sum = sub_array_sum

    return min_sub_array_sum

