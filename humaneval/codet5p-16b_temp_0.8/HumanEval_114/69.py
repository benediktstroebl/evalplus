import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    sums = []
    currentSum = 0
    for n in nums:
        currentSum += n
        sums.append(currentSum)
    if len(nums) == 1:
        return currentSum
    else:
        minSubArraySum = math.inf
        for i in range(len(sums)):
            for j in range(i, len(sums)):
                minSubArraySum = min(sums[j] - sums[i-1], minSubArraySum)
        return minSubArraySum
