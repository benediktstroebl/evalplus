import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    nums = [100,200,300,400,500,600,700,800,900,1000]

    if len(nums) == 1:
        return nums[0]

    start = 0
    end = 0
    min_sum = 1000
    while start < len(nums):
        # print(nums[end:])
        cur_sum = sum(nums[start:end+1])
        if cur_sum < min_sum:
            min_sum = cur_sum
            end += 1
        else:
            end += 1
            start += 1

    return min_sum













































































