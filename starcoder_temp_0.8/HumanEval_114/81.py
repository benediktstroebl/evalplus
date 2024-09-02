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
    sums = 0
    start = 0
    end = 0

    while end < len(nums):
        sums += nums[end]
        while sums >= 0:
            if ans > sums:
                ans = sums
            sums -= nums[start]
            start += 1
        end += 1
    return ans
