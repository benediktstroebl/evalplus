import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    sum = 0
    start = 0
    end = 0
    min_sum = nums[0]
    for index in range(len(nums)):
        sum = sum + nums[index]
        end = index
        while sum > 0 and end - start + 1 > 0:
            if sum < min_sum:
                min_sum = sum
            sum = sum - nums[start]
            start += 1
    return min_sum


