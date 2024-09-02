import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    nums = list(nums)
    left, right = 1, max(nums)
    while left <= right:
        mid = (left + right) // 2
        sum = mid
        for i in range(1, len(nums)):
            if nums[i] > sum:
                sum += nums[i]
        if sum == len(nums) + 1:
            print(sum)
            return sum
        left = mid + 1
    return left

nums = [2, 3, 4, 1, 2, 4]
