import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    min_sum = math.inf
    left = 0
    right = 1
    i = 0
    sum_num = 0
    while right <= len(nums) and left <= right:
        if right - left > 1:
            sum_num -= nums[i]
            i += 1
            if sum_num < min_sum:
                min_sum = sum_num

        sum_num += nums[right]
        right += 1

        if left == right:
            if nums[left] < min_sum:
                min_sum = nums[left]

        if sum_num < min_sum:
            min_sum = sum_num

        if left < right:
            left += 1

    return min_sum
