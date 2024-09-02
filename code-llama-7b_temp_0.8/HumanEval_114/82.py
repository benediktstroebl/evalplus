import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    length = len(nums)
    if length == 1:
        return nums[0]

    min_sum = math.inf
    # 滑动窗口
    for i in range(length):
        cur_sum = 0
        for j in range(i, length):
            cur_sum += nums[j]
            min_sum = min(min_sum, cur_sum)
            if cur_sum <= 0:
                break
    return min_sum
