import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    nums_sum = sum(nums)
    if len(nums) == 1:
        return nums_sum

    min_sum = math.inf
    curr_sum = 0

    # Iterate through the array, adding current to current sum until we reach a sum
    # greater than the previous minimum sum
    for num in nums:
        curr_sum += num
        if curr_sum < min_sum:
            min_sum = curr_sum
        if curr_sum > 0:
            curr_sum = 0

    # If we get to the end and no sum is smaller than the previous minimum, return
    # the previous minimum sum
    if min_sum == math.inf:
        return 0
    return min_sum

