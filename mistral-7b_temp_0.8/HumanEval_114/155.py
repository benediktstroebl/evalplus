import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # nums = [2, 3, 4, 1, 2, 4]
    # nums = [-1, -2, -3]
    # nums = [1, 2, 3, 4]

    # cur_sum = 0
    # res = math.inf
    # for num in nums:
    #     cur_sum += num
    #     res = min(res, cur_sum)
    # return res

    # TLE
    res = nums[0]
    for i in range(1, len(nums)):
        for j in range(i):
            cur_sum = nums[i] + sum(nums[j:i])
            res = min(res, cur_sum)
    return res

