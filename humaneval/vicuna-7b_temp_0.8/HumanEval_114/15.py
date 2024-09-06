import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # Use a 2D list to keep track of the minimum sum of sub-arrays
    # that is less than or equal to the current sub-array
    min_sum_2d = [[float('inf')] * len(nums) for _ in range(len(nums))]
    for i in range(1, len(nums)):
        for j in range(i):
            min_sum_2d[i][j] = math.min(nums[i], nums[j])
        min_sum_2d[i][i] = min_sum_2d[i - 1][i] + nums[i]
    # Iterate through the sub-arrays
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] >= min_sum_2d[i][j]:
                min_sum_2d[i][j] = nums[i] + nums[j]
    # The minimum sum of sub-arrays is the sum of the elements in the first row of the 2D list
    return sum(min_sum_2d[0])

nums = [2, 3, 4, 1, 2, 4]
