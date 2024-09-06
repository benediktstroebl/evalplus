import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    ans = math.inf
    cur_sum = 0

    for num in nums:
        if num + cur_sum < ans:
            ans = num + cur_sum
        cur_sum += num

    return ans
