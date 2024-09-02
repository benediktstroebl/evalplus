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

    # result is the sum of all elements
    result = sum(nums)
    # current sum that starts at the first element of the array
    current = nums[0]

    # we can just iterate over the list. if the current sum is less than the
    # result, we can update the result to be the current sum
    for i in range(1, len(nums)):
        current += nums[i]
        if current < result:
            result = current

    return result

