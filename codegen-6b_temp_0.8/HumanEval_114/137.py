import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # Get sum of all numbers
    sum = 0

    for num in nums:
        sum += num

    # Get minimum sum of subarray
    min_sum = sum
    for i in range(1, len(nums)):
        start = i
        end = i + 1

        while end <= len(nums):
            # Get sum of subarray
            sum = 0
            for num in nums[start:end]:
                sum += num

            if sum < min_sum:
                min_sum = sum

            end += 1

    return min_sum

