import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # write your code here
    if nums is None:
        return None
    if len(nums) == 0:
        return None
    minSum = nums[0]
    sum = 0
    left = 0
    right = 0
    while left < len(nums):
        if nums[right] is None:
            right = right + 1
            continue
        if right >= len(nums):
            break
        sum = sum + nums[right]
        right += 1

        if sum < minSum:
            minSum = sum
        if right - left > 1:
            sum = sum - nums[left]
            left += 1
    return minSum
