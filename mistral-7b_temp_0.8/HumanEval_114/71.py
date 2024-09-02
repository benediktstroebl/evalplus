import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # corner case: empty list
    if len(nums) == 0:
        return 0

    # corner case: single element
    if len(nums) == 1:
        return nums[0]

    # corner case: two elements
    if len(nums) == 2:
        return min(nums[0], nums[1])

    # start traversing from the left of the list
    min_sum = nums[0]
    # start with the second element to have a valid subarray
    for i in range(1, len(nums)):
        # if we have a valid subarray, it's sum will be the current element plus the previous min_sum
        min_sum = min(min_sum + nums[i], nums[i])
    return min_sum

