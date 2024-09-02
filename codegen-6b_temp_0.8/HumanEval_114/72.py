import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # if not nums:
    #     return 0
    # start = 0
    # end = 0
    # curr_min = 0
    # curr_sum = 0
    # for i in range(0, len(nums)):
    #     curr_sum += nums[i]
    #     while curr_sum < 0:
    #         curr_sum -= nums[start]
    #         start += 1
    #     if curr_sum < curr_min:
    #         curr_min = curr_sum
    #     end = i
    # return curr_min
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    curr_min = math.inf
    curr_sum = 0
    for i in range(0, len(nums)):
        curr_sum += nums[i]
        while curr_sum < 0:
            curr_sum -= nums[0]
            nums.pop(0)
        if curr_sum < curr_min:
            curr_min = curr_sum
    return curr_min
