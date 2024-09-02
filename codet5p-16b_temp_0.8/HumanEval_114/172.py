import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    if len(nums) == 0:
        return 0
    else:
        min_sum = math.inf
        temp_sum = 0
        i = 0
        j = 0
        while i < len(nums):
            while j < len(nums):
                temp_sum = sum(nums[i:j])
                if temp_sum < min_sum:
                    min_sum = temp_sum
                j += 1
            i += 1
            j = i
        return min_sum
