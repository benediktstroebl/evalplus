import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # keep track of the minimum sum
    sum = nums[0]
    # check each number in the array
    for num in nums[1:]:
        # if the sum is less than the current sum, update the sum
        if sum - num >= sum:
            sum = num
    return sum
