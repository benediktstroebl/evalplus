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

    if len(nums) == 2:
        return min(nums[0], nums[1])

    arr = [float('inf')] * (len(nums) + 1)
    arr[0], arr[1] = 0, nums[0]

    for i in range(2, len(nums) + 1):
        arr[i] = min(arr[i - 1], arr[i - 2]) + nums[i - 1]

    return min(arr[-2:])
