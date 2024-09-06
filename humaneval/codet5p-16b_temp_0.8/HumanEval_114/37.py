import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    nums_sum = math.inf
    if len(nums) == 0:
        return 0
    elif len(nums) == 1:
        return nums[0]
    elif len(nums) == 2:
        return min(nums[0], nums[1])
    else:
        for i in range(len(nums)):
            sum_nums = nums[i]
            for j in range(i+1, len(nums)):
                sum_nums += nums[j]
                if sum_nums < nums_sum:
                    nums_sum = sum_nums
        return nums_sum

