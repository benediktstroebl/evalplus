import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    
    sums = [0] * len(nums)
    total = 0
    for idx, num in enumerate(nums):
        total += num
        sums[idx] = total
    
    total = math.inf
    left = right = 0
    for right in range(len(nums)):
        total = min(total, sums[right])
        while total >= sums[left]:
            total -= sums[left]
            left += 1
    
    return total
