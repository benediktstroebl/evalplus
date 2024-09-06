import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    left = 0
    right = 0
    minSubarraySum = nums[0]

    while right < len(nums):
        minSubarraySum += nums[right]
        while left < right and minSubarraySum > 0:
            minSubarraySum -= nums[left]
            left += 1

        minSubarraySum = min(minSubarraySum, nums[right])
        right += 1

    return minSubarraySum

