import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    # Since we need the minimum sum of the subarray, we can't just start at 0
    currentSum = nums[0]
    minSum = nums[0]
    for num in nums[1:]:
        currentSum = min(num, currentSum + num)
        minSum = min(currentSum, minSum)

    return minSum
