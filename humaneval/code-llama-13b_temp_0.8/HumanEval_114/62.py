import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # first we need to find the max size of the subarray
    array_length = len(nums)
    maximum = math.floor(array_length / 2)

    if array_length == 1:
        return nums[0]

    minimum = float("inf")
    # try every combination
    for i in range(maximum, 0, -1):
        for j in range(array_length - i + 1):
            # make sure the minimum value is always updated
            if sum(nums[j:j + i]) < minimum:
                minimum = sum(nums[j:j + i])

    return minimum
