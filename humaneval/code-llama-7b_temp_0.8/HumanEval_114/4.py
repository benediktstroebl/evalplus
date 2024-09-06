import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    # Compute the sum of all elements in the array
    nums_sum = 0
    for num in nums:
        nums_sum += num

    # Compute the minimum sub-array sum
    if len(nums) < 2:
        return nums_sum

    # If all elements in nums are negative, return the maximum possible
    # sub-array sum
    min_sub_array_sum = nums_sum
    for num in nums:
        if num >= 0:
            return nums_sum
    return min_sub_array_sum

