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

    res = 0
    min_res = 10000
    l = len(nums)

    if l == 1:
        res = nums[0]
        return res

    for i in range(0, l-1):
        for j in range(i+1, l):
            if j - i == 1:
                res = nums[i] + nums[j]
            else:
                res = nums[i] + nums[j] - nums[j-1]
            if res < min_res:
                min_res = res
    return min_res

