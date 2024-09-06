import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # DP
    # dp = [nums[0]]
    # for i in range(1, len(nums)):
    #     dp.append(min(nums[i], nums[i] + dp[-1]))
    # return min(dp)
    # Sort and binary search
    nums.sort()
    target = sum(nums)
    minSubArraySum = target
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if target - nums[j] >= 0:
                minSubArraySum = min(target - nums[j], minSubArraySum)
            else:
                break
    return minSubArraySum


