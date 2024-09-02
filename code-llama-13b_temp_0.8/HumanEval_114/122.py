import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # two pointers solution
    left, right = 0, 0
    total = 0
    ans = math.inf
    while right < len(nums):
        total += nums[right]
        ans = min(ans, total - max(nums[left:right+1]))
        right += 1
        if total < 0:
            left = right
            total = 0

    return ans
