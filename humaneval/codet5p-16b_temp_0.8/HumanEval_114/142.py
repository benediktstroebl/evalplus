import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    total = 0
    minimum = math.inf
    left = 0
    right = 0

    while right < len(nums):
        total += nums[right]
        right += 1

        while total >= minimum:
            minimum = total if total < minimum else minimum
            total -= nums[left]
            left += 1

    return minimum if minimum!= math.inf else 0

