import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # find the largest positive integer that can be subtracted from the array
    # sum to find the minimum sub-array sum
    # O(n) runtime, O(1) space
    smallest = float('inf')
    for i in range(len(nums)):
        total = 0
        for num in nums[i:]:
            total += num
            smallest = min(total, smallest)
    return smallest if smallest < float('inf') else 0
