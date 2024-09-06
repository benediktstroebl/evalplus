import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    total = 0
    sum = math.inf
    l = 0
    for r in range(len(nums)):
        total += nums[r]
        while total >= sum:
            sum = min(sum, total-sum+nums[l])
            l += 1
    return sum if sum!= math.inf else 0
