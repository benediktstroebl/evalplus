import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    min = math.inf
    size = len(nums)
    if size == 1:
        return nums[0]
    for i in range(size):
        if i > 0:
            nums[i] = nums[i] + nums[i - 1]
        curMin = nums[i]
        if i == size - 1:
            break
        for j in range(i + 1, size):
            curMin = nums[j] - nums[i]
            if curMin < min:
                min = curMin
    return min

