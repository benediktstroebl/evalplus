import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # Calculate the sum of the entire array
    # sum_of_array = sum(nums)
    # if the sum is zero, return zero
    # if the array has a single element, return that element
    # else:
    #     add the first and last element
    #     if that sum is zero, add the sum of all the elements in the middle
    #     else:
    #         add the two halves

    sum_of_array = sum(nums)

    if sum_of_array == 0:
        return 0

    if len(nums) == 1:
        return nums[0]

    start = 0
    end = len(nums) - 1
    sum_of_first_and_last = nums[start] + nums[end]

    if sum_of_first_and_last == 0:
        return sum_of_first_and_last + sum(nums[1:-1])

    return min(sum_of_array, sum_of_first_and_last,
               sum(nums[1:-1]) + sum(nums[:start]),
               sum(nums[1:-1]) + sum(nums[end+1:]))

