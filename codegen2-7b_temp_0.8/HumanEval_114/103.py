import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    if nums is None or len(nums) == 0:
        return 0

    solution = math.inf
    for i in range(len(nums)):
        currentSum = nums[i]
        minSum = currentSum

        for j in range(i + 1, len(nums)):
            currentSum += nums[j]

            if currentSum < minSum:
                minSum = currentSum

        solution = min(solution, min
