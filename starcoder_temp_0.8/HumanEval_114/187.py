import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    min = 0
    max = 0
    suma = 0
    for i in range(len(nums)):
        suma += nums[i]
        if suma < 0:
            suma = 0
            max = 0
            continue
        if suma > max:
            max = suma
        if max > min:
            min = max
    return min
