import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # 1) if len == 1, return element 
    # 2) start with first element, iterate over rest, check if sum of current ele 
    # and next ele is larger than next ele, if so, add to array and check if sum 
    # of current array is less than min
    # 3) repeat from 2) with next ele and add to array
    # 4) repeat until end of array

    i = 0
    min = math.inf
    curr_min = 0
    while i < len(nums):
        curr_min = nums[i]
        j = i + 1
        while j < len(nums):
            if curr_min + nums[j] < nums[j]:
                curr_min += nums[j]
            if curr_min < min:
                min = curr_min
            j += 1
        i += 1
    return min

