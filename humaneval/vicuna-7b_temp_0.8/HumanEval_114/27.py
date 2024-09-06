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
    # sort the array in non-descending order
    nums = sorted(nums)
    # initialize the sum of the array
    sum = 0
    # loop through the array
    for i in range(n):
        # if the current element is not 0 and the sum of the sub-array is greater than the current element,
        # we can update the sum of the sub-array
        if nums[i] != 0 and sum + nums[i] > nums[i]:
            sum = nums[i]
            # initialize the new sub-array
            new_nums = nums[i:]
            # if the new array is not empty, we have found a valid sub-array
            if len(new_nums) > 0:
                # update the minimum sum of sub-array
                min_sum = sum + new_nums[0]
                # if the new array is not a subset of the original array, we have found the minimum sum of sub-array
                if new_nums != nums:
                    return min_sum
            # reset the sum of the sub-array
            sum = 0
    return sum