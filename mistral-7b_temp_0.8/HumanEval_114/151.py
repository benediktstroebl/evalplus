import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # write your code here
    min_sum = math.inf
    sub_sum = 0
    start = 0
    for end in range(len(nums)):
        sub_sum += nums[end]
        while sub_sum > 0 and sub_sum >= min_sum:
            sub_sum -= nums[start]
            start += 1
        min_sum = min(min_sum, sub_sum)
    return min_sum if min_sum < math.inf else 0
