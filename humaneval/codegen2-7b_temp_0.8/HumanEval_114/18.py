import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    start = end = sum = 0
    min_sum = math.inf

    for i, num in enumerate(nums):
        sum += num

        if end < sum:
            end = sum
            start = end - sum
        else:
            end = sum

        if sum < min_sum:
            min_sum = sum

    return min_sum if min_sum!= math.inf else
