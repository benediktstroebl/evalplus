import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    if not nums:
        return 0
    ans = math.inf
    cur_sum = 0
    for i in nums:
        cur_sum += i
        ans = min(ans, cur_sum)
        if cur_sum < 0:
            cur_sum = 0
    if ans == math.inf:
        return 0
    
