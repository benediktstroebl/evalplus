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
    nums = [math.inf] + nums
    left = 0
    right = 0
    summ = nums[0]
    minimum = math.inf
    for left in range(1, n+1):
        while right < left and summ >= minimum:
            summ -= nums[left]
            left += 1
        summ += nums[right]
        if summ < minimum:
            minimum = summ
        right += 1
    return minimum
