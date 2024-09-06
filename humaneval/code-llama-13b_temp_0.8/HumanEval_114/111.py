import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    if len(nums) == 0:
        return 0

    min_sum = math.inf
    i = 0
    j = len(nums) - 1

    while i < j:
        # make sure the smallest sum is at the beginning of the array
        if nums[i] > nums[j]:
            i += 1
        else:
            j -= 1

        # update min_sum
        if j - i < 2:
            min_sum = min(min_sum, sum(nums[i : j + 1]))
        else:
            min_sum = min(min_sum, sum(nums[i : i + 2]) + minSubArraySum(nums[i + 2 : j + 1]))

    return min_sum
