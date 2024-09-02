import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    padded = [0] + nums
    cumulative = []
    for i in range(len(padded)):
        if i == 0:
            cumulative.append(0)
        else:
            cumulative.append(cumulative[-1] + padded[i])
    min_sum = math.inf
    total = cumulative[-1]
    for start in range(len(padded)):
        for end in range(start, len(padded)):
            if start > end:
                continue
            total = cumulative[end] - cumulative[start]
            min_sum = min(min_sum, total)
    return min_sum

