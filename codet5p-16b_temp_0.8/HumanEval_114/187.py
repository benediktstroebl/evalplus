import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    
    if len(nums) == 0:
        return 0
    
    total_sum = 0
    min_subarray_sum = math.inf
    
    for n in nums:
        total_sum += n
        
        while total_sum >= min_subarray_sum:
            min_subarray_sum = min(min_subarray_sum, total_sum)
            total_sum -= nums[0]
            nums.pop(0)
        
    return min_subarray_sum
