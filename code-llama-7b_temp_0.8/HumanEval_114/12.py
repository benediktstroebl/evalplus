import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # print('nums',nums)
    s = 0
    mini = math.inf
    for num in nums:
        # print(num)
        s += num
        if s < mini:
            mini = s
        if s < 0:
            s = 0
    if mini == math.inf:
        mini = 0
    return mini
