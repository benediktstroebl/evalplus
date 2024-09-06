import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    
    n = len(nums)

    min_sum = sys.maxsize
    for i in range(n):
        for j in range(i,n):
            sum = 0
            for k in range(i,j+1):
                sum += nums[k]
            if sum < min_sum:
                min_sum = sum
    if min_sum == sys.maxsize:
        return 0
    return min_sum
