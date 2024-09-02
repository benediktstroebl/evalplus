import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    if nums == []:
        return 0

    if len(nums) == 1:
        return nums[0]

    res = math.inf
    l, r = 0, 1
    while r < len(nums):
        curr_sum = 0
        for i in range(l, r+1):
            curr_sum += nums[i]
        res = min(res, curr_sum)
        r += 1
        if r == len(nums):
            return res
    return res

