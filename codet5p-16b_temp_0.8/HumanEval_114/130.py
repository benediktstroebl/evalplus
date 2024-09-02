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
        return 0

    minSum = math.inf
    subSum = 0
    left = 0
    for right in range(len(nums)):
        subSum += nums[right]
        while subSum >= nums[left]:
            minSum = min(minSum, subSum - nums[left])
            subSum -= nums[left]
            left += 1
    return minSum
