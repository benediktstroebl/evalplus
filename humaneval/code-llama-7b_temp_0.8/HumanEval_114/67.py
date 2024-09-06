import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    """
    # Doesn't work
    min_sum = math.inf
    left_idx = 0
    right_idx = len(nums) - 1

    while left_idx < right_idx:
        sub_sum = 0
        for i in range(left_idx, right_idx+1):
            sub_sum += nums[i]
            if sub_sum < min_sum:
                min_sum = sub_sum
        if nums[left_idx] > nums[right_idx]:
            left_idx += 1
        else:
            right_idx -= 1
    return min_sum
    """
    min_sum = math.inf
    curr_sum = 0
    for i in nums:
        curr_sum += i
        if curr_sum < min_sum:
            min_sum = curr_sum
        if curr_sum > 0:
            curr_sum = 0
    return min_sum
