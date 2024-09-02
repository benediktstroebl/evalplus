import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    for i in range(len(nums)):
        for j in range(i):
            sum = nums[i] + nums[j]
            if sum > nums[i]:
                continue
            if sum + nums[i+1] < nums[i]:
                break
            nums[i] = sum
            sum = 0
            for num in nums[i+1:]:
                sum += num
            if sum >= nums[i]:
                continue
            return sum
    return 0
