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
    sum = 0
    for num in nums:
        sum += num
        if sum < min_sum:
            min_sum = sum
        if sum > min_sum:
            sum = sum - nums[i]
    return min_sum
