import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    n = len(nums)
    min_diff = math.inf
    current_sum = 0
    smallest_index = -1
    current_index = 0
    for num in nums:
        current_sum += num
        while current_sum >= nums[0] and current_sum - nums[smallest_index] < min_diff:
            min_diff = current_sum - nums[smallest_index]
            current_index = smallest_index
        if current_sum - nums[smallest_index] < min_diff:
            min_diff = current_sum - nums[smallest_index]
            current_index = smallest_index
        if current_sum < nums[0]:
            smallest_index += 1
        current_index += 1
    return min_diff
