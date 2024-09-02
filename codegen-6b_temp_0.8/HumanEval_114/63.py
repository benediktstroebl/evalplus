import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    if len(nums) < 2:
        return 0

    running = sum(nums[0:len(nums)-1])
    start = min(0, running)
    end = start + 1

    print running

    while end < len(nums):
        running = running - nums[start] + nums[end]
        if running < 0:
            running = 0

        start = start + 1
        end = end + 1

    return sum(nums[start:end])
