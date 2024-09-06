import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    if not nums:
        return 0

    # start with the largest number
    # end with the smallest number
    best = nums[0]
    min_sum = math.inf

    # max_sum
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            min_sum = min(nums[i:j+1])
            break

    return min_sum



