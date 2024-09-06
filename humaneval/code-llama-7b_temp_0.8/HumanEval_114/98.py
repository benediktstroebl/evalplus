import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    if len(nums) == 1:
        return nums[0]
    left = 0
    right = 1
    minSubArraySum = float('inf')
    currentSubArraySum = nums[left] + nums[right]
    while right < len(nums):
        if currentSubArraySum >= 0:
            minSubArraySum = min(minSubArraySum, currentSubArraySum)
            right += 1
            currentSubArraySum = currentSubArraySum - nums[left] + nums[right]
        elif currentSubArraySum < 0:
            currentSubArraySum = nums[right]
            left = right
            right += 1
    if currentSubArraySum < 0:
        currentSubArraySum = nums[left] + nums[right]
    minSubArraySum = min(minSubArraySum, currentSubArraySum)
    return minSubArraySum
    



