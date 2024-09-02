import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    big_sum = sum(nums)

    if big_sum == 0:
        return 0

    if big_sum < 0:
        big_sum = -big_sum

    least_sum = big_sum
    for i in range(1, len(nums)):
        curr_sum = sum(nums[:i])
        new_sum = curr_sum - nums[i]
        if new_sum < least_sum:
            least_sum = new_sum

    if least_sum == big_sum:
        return 0

    return least_sum
