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
    
    min_sum = math.inf
    start = 0
    end = 0
    sum = 0
    while end < len(nums):
        sum += nums[end]
        end += 1
        while sum >= nums[start]:
            min_sum = min(sum - nums[start], min_sum)
            sum -= nums[start]
            start += 1
    return min_sum

