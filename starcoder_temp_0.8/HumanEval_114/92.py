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
    if len(nums) == 1:
        return nums[0]
    sum = 0
    min = math.inf
    for i in range(len(nums)):
        sum += nums[i]
        while sum >= 0:
            min = min if min < sum else sum
            sum -= nums[i]
            i += 1
            if i == len(nums):
                break
    return min
