import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    min_sum = float("inf")
    sums = [0]
    for num in nums:
        sums.append(sums[-1] + num)
    for i in range(len(nums) + 1):
        for j in range(i + 1, len(nums) + 1):
            if sums[j] - sums[i] < min_sum:
                min_sum = sums[j] - sums[i]

    return min_sum
