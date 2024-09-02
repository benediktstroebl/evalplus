import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # time complexity O(n)
    # space complexity O(1)
    s = nums[0]
    start = 0
    end = 0
    for i in range(1, len(nums)):
        if s > 0:
            s += nums[i]
        else:
            start = i
            s = nums[i]
            end = i
    if s > 0:
        return 0
    return nums[start:end + 1]
