import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    result = float('inf')
    dp = [float('inf') for _ in range(len(nums)+1)]
    dp[0] = 0
    for i in range(len(nums)):
        dp[i+1] = dp[i] + nums[i]

    for i in range(len(dp)-1, -1, -1):
        if dp[i] > 0:
            result = min(result, dp[i])

    return result

assert(minSubArraySum([2, 3, 4, 1, 2, 4]) == 1)
assert(minSubArraySum([-1, -2, -3]) == -6)
assert(minSubArraySum([-2, -1, -4, -6, -8, -9]) == -7)
assert(minSubArraySum([]) == 0)
assert(minSubArraySum([5]) == 5)
assert(minSubArraySum([-2,1,-3,4,-1,2,1,-5,4]) == 6)
assert(minSubArraySum([1,2,3]) == 0)
assert(minSubArraySum([1,2,3,1]) == 0)
assert(minSubArraySum([1,2,3,1,2]) == 0)
assert(minSubArraySum([1,2,-1,4,5,3,-2,1]) == 4)
assert(minSubArraySum([-1,-5,-2,-4]) == -6)
assert(minSubArraySum([-1,-2,-3]) == -6)
assert(minSubArraySum([-1]) == -1)
assert(minSubArraySum([1,-2,1,-5,1,-2,-3]) == -2)
assert(minSubArraySum([1,-2,-1,-5,1,-2,-3]) == -1)
assert(minSubArraySum(range(-1, 2)) == 0)
assert(minSubArraySum(range(-1, -1)) == -1)
assert(minSubArraySum(range(3, -3, -1)) == -3)
assert(minSubArraySum(range(-3, -3, -1