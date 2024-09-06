import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # TODO: https://leetcode.com/problems/minimum-subarray-sum/discuss/193868/Short-Python-DP-solution-O(N)-time
    s = 0
    s_min = None
    for num in nums:
        s += num
        if s_min is None or s < s_min:
            s_min = s
    return s_min
