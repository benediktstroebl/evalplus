import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    length = len(nums)
    left = length
    right = length
    left_sum = 0
    right_sum = 0
    left_min = nums[0]
    right_min = nums[length - 1]
    while left < right:
        if left_min > 0:
            left_sum += left_min
        if right_min > 0:
            right_sum += right_min
        if left_sum < right_min:
            left += 1
            left_min = nums[left]
        elif left_sum > right_min:
            right -= 1
            right_min = nums[right]
        else:
            break

    return left_sum + right_sum

