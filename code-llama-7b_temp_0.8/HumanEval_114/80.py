import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    sum_all = 0
    for num in nums:
        sum_all += num

    if len(nums) == 1:
        return nums[0]

    min_sum = math.inf

    for i in range(0, len(nums)):
        sum_temp = nums[i]
        for j in range(i+1, len(nums)):
            sum_temp += nums[j]
            if sum_temp < min_sum:
                min_sum = sum_temp
            if sum_temp > sum_all - sum_temp:
                break

    return min_sum
