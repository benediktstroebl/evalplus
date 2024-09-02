import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    l_sum = 0
    r_sum = 0
    s_sum = float("inf")
    i = 0
    j = 0
    n = len(nums)
    while j < n:
        if r_sum + nums[j] < nums[j]:
            r_sum += nums[j]
            j += 1
        else:
            r_sum = nums[j]
            j += 1
        while l_sum + r_sum > s_sum and i <= j:
            l_sum -= nums[i]
            i += 1
        s_sum = min(s_sum, l_sum + r_sum)
    return s_sum if s_sum!= float("inf") else 0
