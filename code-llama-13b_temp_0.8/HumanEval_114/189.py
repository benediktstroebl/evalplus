import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    minSum = math.inf
    left, right = 0, 1
    sum = nums[0]
    while left < len(nums):
        while right < len(nums) and sum >= 0:
            sum += nums[right]
            right += 1

        minSum = min(minSum, sum)
        sum += nums[left]
        left += 1
        sum -= nums[left-1]
    return minSum
