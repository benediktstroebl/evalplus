import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    n = len(nums)
    sums = []
    min_sum = math.inf
    min_sum_end_idx = -1

    for start in range(n):
        for end in range(start, n):
            sums.append(sum(nums[start:end+1]))
            if sums[-1] < min_sum:
                min_sum = sums[-1]
                min_sum_end_idx = end + 1
    return nums[min_sum_end_idx: min_sum_end_idx+1]
