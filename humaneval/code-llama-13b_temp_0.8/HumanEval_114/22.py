import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    if nums == None:
        return 0
    if nums == []:
        return math.inf
    min_sum = math.inf
    sum_array = 0
    for num in nums:
        sum_array += num
        min_sum = min(sum_array, min_sum)
        if sum_array > 0:
            sum_array = 0
    return min_sum


