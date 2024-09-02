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
    elif len(nums) == 1:
        return nums[0]
    else:
        start_index = 0
        min_sum = float('inf')
        while start_index < len(nums):
            curr_sum = 0
            for j in range(start_index, len(nums)):
                curr_sum += nums[j]
                if curr_sum < min_sum:
                    min_sum = curr_sum
            start_index += 1
        return min_sum

