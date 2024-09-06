import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    def s_arr(array):
        return sum(array)
    def min_sub(array):
        min_value = math.inf
        min_sum = 0
        for i in array:
            min_sum += i
            if min_value > min_sum:
                min_value = min_sum
            if min_sum < 0:
                min_sum = 0
        return min_value
    min_sum = min_sub(nums)
    if min_sum < 0:
        return min_sum
    else:
        return minSubArraySum(nums[1:])
