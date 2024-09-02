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
    temp = [0] * len(nums)
    for i in range(len(temp)):
        temp[i] = nums[i]
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if j == len(nums) - 1:
                break
            temp[j] += nums[j + 1]
    print(temp)
    min_sum = math.inf
    for i in range(len(temp)):
        min_sum = min(temp[i], min_sum)
    return min_sum
