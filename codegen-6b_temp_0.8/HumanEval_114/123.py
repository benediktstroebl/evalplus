import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    sums = [0]
    s = 0
    for x in nums:
        s += x
        sums.append(s)
    min_sum = sums[-1]
    for i in range(len(sums)):
        for j in range(i, len(sums)):
            sub_sum = sums[j-i] - sums[i]
            min_sum = min(min_sum, sub_sum)
    return min_sum

