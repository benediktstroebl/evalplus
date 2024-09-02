import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    left = 1 + 1
    right = len(nums) - 1
    current = [nums[0]]
    while left < right:
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1] and nums[i] != 0:
                current.append(nums[i])
                current.append(nums[i-1])
                sub_sum = current[-1] + current[-2]
                if sub_sum < left:
                    left = sub_sum
                current = [current[-2]]
            elif nums[i] == 0:
                current.append(nums[i])
                if current[-1] + current[-2] < left:
                    left = current[-1] + current[-2]
                current = [current[-2]]
            else:
                current.append(nums[i])
        left = current[-1]
        current = [current[-2]]
    return left