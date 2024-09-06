import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # Edge Case
    if len(nums) == 0:
        return 0

    """
    To solve this problem, we will use a sliding window approach.
    I.e, we will iterate through the array and at each step we will
    calculate the current minimum subarray sum in the window.
    To do that, we will keep track of the window sum and the minimum
    sum of the subarray so far.
    """
    current_sum = 0
    min_sum = math.inf
    for num in nums:
        current_sum += num
        min_sum = min(current_sum, min_sum)

        if current_sum < 0:
            current_sum = 0

    return min_sum

