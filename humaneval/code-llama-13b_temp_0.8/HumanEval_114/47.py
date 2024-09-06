import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    # min sum of array
    min_sum = math.inf

    # i - starting index
    # j - ending index
    for i in range(len(nums)):
        # Sum of sub-array
        curr_sum = 0

        for j in range(i, len(nums)):
            curr_sum += nums[j]
            min_sum = min(min_sum, curr_sum)

    return min_sum
