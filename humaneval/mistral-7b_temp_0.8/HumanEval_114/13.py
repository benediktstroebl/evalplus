import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    if not nums:
        return 0
    min_sum = math.inf
    min_length = math.inf
    current_sum = 0
    for num in nums:
        current_sum += num
        if current_sum >= min_sum:
            min_sum = current_sum
            min_length = 1
        elif current_sum > min_sum:
            min_length += 1
            current_sum = nums[min_length - 1]
    return min_sum
