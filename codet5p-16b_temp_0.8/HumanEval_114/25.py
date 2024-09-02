import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    if len(nums) == 0:
        return 0
    if len(nums) == 1:
        return nums[0]
    result = math.inf
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i <= j:
                pass
            else:
                sub = nums[i:j+1]
                sub_sum = sum(sub)
                if sub_sum < result:
                    result = sub_sum
    return result

