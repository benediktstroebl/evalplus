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

    min_so_far = nums[0]
    max_so_far = nums[0]

    for i in range(1, len(nums)):
        if nums[i] > 0:
            max_so_far = max(max_so_far+nums[i], nums[i])
            min_so_far = min(nums[i], min_so_far)
        elif nums[i] < 0:
            max_so_far = max(max_so_far+nums[i], nums[i])
            min_so_far = min(min_so_far+nums[i], nums[i])

    return max_so_far
