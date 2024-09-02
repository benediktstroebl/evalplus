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
    min_sum = math.inf
    for num in nums:
        sums.append(sums[-1] + num)
        i = 1
        while i <= len(nums):
            sub_sum = sums[i] - sums[i - 1]
            if sub_sum < min_sum:
                min_sum = sub_sum
            i += 1
    return min_sum

