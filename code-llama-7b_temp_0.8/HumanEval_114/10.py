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
    if n == 1:
        return nums[0]
    if n == 2:
        return min(nums[0], nums[1])
    
    s1 = nums[0]
    s2 = nums[1]
    s3 = s1 + s2
    m = s3
    for i in range(2, n):
        s1 = s2
        s2 = s3
        s3 = s1 + nums[i]
        if s3 < m:
            m = s3
    return m

