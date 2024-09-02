import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    if nums is None:
        return None
    minSum = math.inf
    index = 0
    while index < len(nums):
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            if nums[0] + nums[1] < minSum:
                minSum = nums[0] + nums[1]
            return minSum
        else:
            minSum = nums[index]
            index += 1
            while index < len(nums):
                if minSum > nums[index]:
                    minSum = nums[index]
                else:
                    minSum = minSum + nums[index]
                index += 1
            if minSum < minSum:
                minSum = minSum
            return minSum
