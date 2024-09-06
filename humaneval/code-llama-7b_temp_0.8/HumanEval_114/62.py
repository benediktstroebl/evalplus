import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    sub_array = []
    min_sum = math.inf
    for i in nums:
        sub_array.append(i)
        sub_array = list(filter(lambda x: x <= 0, sub_array))
        sum_array = sum(sub_array)
        if sum_array < min_sum:
            min_sum = sum_array
        if sum_array > 0:
            sub_array.clear()
    return min_sum
