import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    left, right = 1, nums[0]
    for i in range(1, len(nums)):
        if nums[i] < nums[left]:
            left = i
        else:
            right = i
    subarr = nums[left:right+1]
    sum = sum(subarr)
    if sum > 0:
        min_sum = sum - 1
        for i in range(len(subarr)):
            if min_sum < subarr[i]:
                min_sum = subarr[i]
        return min_sum
    else:
        return 0

nums = [100, 150, 10, 200, 300, 50, 1000]
