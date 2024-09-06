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
        return math.inf
    
    min_sum = math.inf
    l = 0
    h = 0
    sum = 0
    while h < len(nums):
        sum += nums[h]
        while sum >= 0 and l <= h:
            if sum < min_sum:
                min_sum = sum
            h += 1
            if h >= len(nums):
                break
            sum += nums[h]
        l += 1
        sum -= nums[l - 1]
    return min_sum
