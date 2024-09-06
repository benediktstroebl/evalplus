import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    # Approach 1: Brute Force
    # Time Complexity: O(n^2)
    # Space Complexity: O(1)

    minSum = math.inf
    for i in range(len(nums)):
        subArraySum = 0
        for j in range(i, len(nums)):
            subArraySum += nums[j]
            minSum = min(minSum, subArraySum)
    return minSum

    # Approach 2: Two Pointers
    # Time Complexity: O(n)
    # Space Complexity: O(1)

    minSum = math.inf
    curSum = 0
    for num in nums:
        curSum += num
        minSum = min(minSum, curSum - num)
    return minSum
