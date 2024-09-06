import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    if len(nums) == 0:
        return None

    min_sum = math.inf
    left = 0
    right = 1
    # The window size will go from 2 to N
    while right < len(nums):
        # Keep shrinking the window as long as we are decreasing the sum
        window_sum = sum(nums[left:right])
        if window_sum < min_sum:
            min_sum = window_sum
            left += 1
            right += 1
        else:
            right += 1

    return min_sum
