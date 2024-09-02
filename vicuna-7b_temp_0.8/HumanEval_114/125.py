import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # sort nums
    nums = sorted(nums)
    # initialize sum to 0
    sum = 0
    # initialize starting index to 0
    starting_index = 0
    # set ending index to be nums' length - 1
    ending_index = len(nums) - 1
    while starting_index <= ending_index:
        # if sum of current sub-array is less than the current element,
        # move the starting index to the next element
        while sum + nums[starting_index] <= nums[starting_index]:
            starting_index += 1
        # if sum of current sub-array is greater than or equal to the current element,
        # and the ending index is less than the length of the array,
        # check if current sub-array is a valid sub-array
        if starting_index <= ending_index and sum + nums[starting_index] >= nums[starting_index] and ending_index < len(nums):
            # add current sub-array to the result list
            result_list.append(nums[starting_index])
            # update sum to the sum of current sub-array
            sum = sum + nums[starting_index]
            # update starting index to the next element
            starting_index += 1
    return result_list