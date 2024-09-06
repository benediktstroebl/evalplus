import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    # Basic approach
    sum = 0
    min = math.inf

    for num in nums:
        sum += num
        min = min if min < sum else sum
        if sum < 0:
            sum = 0

    return min if min!= math.inf else 0
