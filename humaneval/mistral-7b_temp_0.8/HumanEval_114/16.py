import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    min_sum = math.inf
    #cur_sum = 0
    cur_sum = [0]
    for i in nums:
        cur_sum.append(cur_sum[-1] + i)
    #print(cur_sum)
    #print(cur_sum)
    n = len(nums)
    for i in range(1, n + 1):
        if i > min_sum:
            break
        min_sum = min(min_sum, cur_sum[i] - cur_sum[i - 1])
    #print(min_sum)
    return min_sum


