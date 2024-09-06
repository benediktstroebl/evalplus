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
    while end < len(nums):
        sum = 0
        while end < len(nums) and sum + nums[end] < min_sum:
            sum += nums[end]
            end += 1

        if sum < min_sum:
            min_sum = sum
            start = end - end % len(nums)

        sum = 0
        while start <= len(nums) and sum + nums[start] < min_sum:
            sum += nums[start]
            start += 1

        if sum < min_sum:
            min_sum = sum
            end = start - start % len(nums)

    return min_sum
