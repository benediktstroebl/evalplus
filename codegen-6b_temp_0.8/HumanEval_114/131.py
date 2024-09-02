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
    sum = 0
    min_sum = math.inf
    pre_sum = [0]
    for num in nums:
        pre_sum.append(pre_sum[-1] + num)
        print(pre_sum)
        min_sum = min(min_sum, pre_sum[-1])

    return min_sum
