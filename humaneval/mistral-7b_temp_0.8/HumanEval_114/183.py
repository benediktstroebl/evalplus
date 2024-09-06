import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    curr_sum = 0
    left, right = 0, 1
    min_sum = math.inf
    while right < len(nums):
        curr_sum += nums[right]
        while curr_sum > 0 and left < right:
            min_sum = min(min_sum, curr_sum)
            curr_sum -= nums[left]
            left += 1
        right += 1
    return min_sum


