import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    m, n = len(nums), len(nums[0])
    result = float('inf')
    max_len = m if m > n else n
    for i in range(max_len):
        for j in range(i+1, min(m, n)):
            for k in range(0, j+1):
                sub = [nums[i:j+1] if i+1 < j else [nums[i]]*len(nums[0])+[nums[j]] if j+1 < m else [nums[i]]*(m-len(nums[0]))+[nums[j]]*(n-j-1) for nums in nums]
                result = min(result, sum(sub))
    return result
