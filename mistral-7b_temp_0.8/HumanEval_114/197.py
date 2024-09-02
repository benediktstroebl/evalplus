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
    nums_sum = 0
    left = 0
    right = 0
    while right < len(nums):
        nums_sum += nums[right]
        while nums_sum > 0 and nums[left] <= nums[right]:
            min_sum = min(min_sum, nums_sum)
            nums_sum -= nums[left]
            left += 1
        right += 1
    return min_sum
