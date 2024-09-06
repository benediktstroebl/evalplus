import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    if len(nums) == 1:
        return nums[0]
    else:
        min_sum = math.inf
        current_sum = 0
        for i in range(len(nums)):
            current_sum += nums[i]
            for j in range(i+1, len(nums)+1):
                min_sum = min(min_sum, current_sum)
                current_sum = current_sum - nums[i] + nums[j-1]
        return min_sum
