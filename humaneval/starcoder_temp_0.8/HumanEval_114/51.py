import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    if not nums:
        return 0
    n = len(nums)
    if n == 1:
        return nums[0]

    min_so_far = math.inf
    curr_sum = 0
    start_pos = 0
    for i in range(n):
        curr_sum += nums[i]
        while curr_sum > 0:
            min_so_far = min(min_so_far, curr_sum)
            start_pos += 1
            if start_pos > i:
                break
            curr_sum -= nums[start_pos - 1]

    return min_so_far
