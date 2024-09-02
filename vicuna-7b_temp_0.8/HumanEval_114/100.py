import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # Check if there are any negative numbers in the array
    negative_nums = [x for x in nums if x < 0]
    if negative_nums:
        return -sum(negative_nums)

    min_sum = math.inf
    start, end = 0, 0
    for i in range(1, len(nums)):
        # If current element is less than the current end, update start
        if nums[i] < nums[end]:
            start = i + 1
        # If current element is greater than the current start, update end
        if nums[i] > nums[start]:
            end = i - 1
        # If we have a sub-array with a positive sum, check if it's less than the current min sum
        if start < end and end - start > 0:
            new_sum = sum(nums[start:end])
            if new_sum < min_sum:
                min_sum = new_sum
                start_index = end = start
    return min_sum
