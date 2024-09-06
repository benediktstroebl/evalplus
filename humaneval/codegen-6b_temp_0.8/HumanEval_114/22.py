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

    # Using sliding window method to calculate sum
    # Time: O(n)
    # Space: O(1)
    result = float("inf")
    min_sum = sys.maxint
    current_sum = 0
    for i in xrange(len(nums)):
        current_sum += nums[i]
        if current_sum < min_sum:
            min_sum = current_sum
        if current_sum - min_sum < result - min_sum:
            result = current_sum - min_sum

    return result
