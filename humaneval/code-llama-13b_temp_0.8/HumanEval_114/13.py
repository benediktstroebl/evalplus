import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # use two pointers
    # start is the pointer for sub array, end is the pointer for nums
    start = 0
    end = 0
    current_sum = 0
    min_sum = math.inf

    while end < len(nums):
        # expand sub array
        current_sum += nums[end]
        end += 1
        # shrink sub array
        while current_sum >= min_sum:
            current_sum -= nums[start]
            start += 1
        min_sum = min(min_sum, current_sum)
    return min_sum

