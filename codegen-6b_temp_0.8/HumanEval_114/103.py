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
    min = 0
    curr_min = 0
    seen = [0] * len(nums)
    seen[0] = nums[0]
    for i in range(1, len(nums)):
        if curr_min + nums[i] < 0:
            curr_min = 0
        else:
            curr_min += nums[i]
        min = min if min > curr_min else curr_min
        seen[i] = nums[i] if seen[i-1] >= 0 else 0
        #print("i:", i, "curr_min:", curr_min, "min:", min, "nums[i]", nums[i], "seen[i-1]:", seen[i-1], "seen[i]:", seen[i])

    return min
