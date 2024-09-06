import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    min_sum = math.inf
    min_sum_arr = []
    if len(nums) == 1:
        return nums[0]
    for i in range(len(nums)):
        sum = sum_num = 0
        for j in range(i, len(nums)):
            sum += nums[j]
            sum_num = max(sum_num, sum)
            if sum_num < min_sum:
                min_sum = sum_num
                min_sum_arr = [nums[i:j + 1]]
            elif sum_num == min_sum:
                min_sum_arr.append(nums[i:j + 1])
    return min_sum_arr

