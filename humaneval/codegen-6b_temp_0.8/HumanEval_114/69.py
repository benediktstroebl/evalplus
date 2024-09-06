import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    if not nums: return 0

    min_sum = float("inf")
    limit = len(nums) - 1 # limit is inclusive

    for i in range(len(nums)):
        if i > 0:
            nums[i] += nums[i - 1]
        if nums[i] >= 0:
            min_sum = nums[i]
        for j in range(i + 1, len(nums)):
            if min_sum + nums[j] < 0:
                break
            min_sum += nums[j]
            if min_sum < 0:
                min_sum = 0

            if min_sum < min_sum:
                min_sum = nums[j]

            if min_sum < min_sum:
                continue
            else:
                break

    return min_sum


