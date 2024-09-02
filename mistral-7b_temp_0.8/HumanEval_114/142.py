import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    def solve(nums, idx):
        if idx == 0:
            return nums[idx]
        if idx == 1:
            return min(nums[idx], nums[idx] + nums[idx-1])

        return min(nums[idx], nums[idx] + solve(nums, idx-1), solve(nums, idx-2) + nums[idx-1])

    return solve(nums, len(nums)-1)

