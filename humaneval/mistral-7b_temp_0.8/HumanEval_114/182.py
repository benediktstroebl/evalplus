import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    min_sum = math.inf
    sub_arr = []
    for num in nums:
        if not sub_arr:
            sub_arr.append(num)
        else:
            sub_arr.append(num)
            min_sum = min(min_sum, sum(sub_arr))
            sub_arr = sub_arr[1:]
    if sub_arr:
        min_sum = min(min_sum, sum(sub_arr))
    return min_sum
