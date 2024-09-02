import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    def minSubArray(arr, sum):
        for i in range(len(arr)):
            sub = sum
            if sub == 0:
                return 0
            for j in range(i, len(arr)):
                sub -= arr[j]
                if sub < 0:
                    break
            if sub == 0:
                return min(arr[i], arr[i])
        return
