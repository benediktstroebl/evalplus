import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    
    min_sub_array_sum = None
    sub_array_sum = 0
    for num in nums:
        sub_array_sum += num
        if sub_array_sum <= 0:
            sub_array_sum = 0
        elif min_sub_array_sum == None or sub_array_sum < min_sub_array_sum:
            min_sub_array_sum = sub_array_sum
    return min_sub_array_sum if min_sub_array_sum!= None else 0
