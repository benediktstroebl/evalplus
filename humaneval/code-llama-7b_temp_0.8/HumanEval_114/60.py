import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # The trick is to keep track of the best sum
    # and the current sum
    # Initialise it to be the first element
    best = nums[0]
    cur = nums[0]

    for i in range(1, len(nums)):
        cur = min(cur + nums[i], nums[i])
        best = min(best, cur)
    return best
