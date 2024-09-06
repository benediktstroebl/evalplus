import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # s=0
    # for i in range(len(nums)):
    #     s+=nums[i]
    # return s
    # return sum(nums)
    if nums == []:
        return 0
    sum = 0
    min_ = 0
    for i in nums:
        sum += i
        if min_ < sum:
            min_ = sum
        if sum < 0:
            sum = 0
    return min_
