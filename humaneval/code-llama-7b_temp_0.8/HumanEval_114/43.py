import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    min_val = math.inf
    min_sum = 0
    for i in range(len(nums)):
        min_val = nums[i]
        break
    min_sum += min_val
    # for i in range(1, len(nums)):
    #     if nums[i] < nums[i - 1]:
    #         min_val = nums[i]
    #         break
    # min_sum += min_val
    print(min_sum)
    return min_sum


