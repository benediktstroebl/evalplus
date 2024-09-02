import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # Do not write main() function.
    # Do not import array or use array as a global variable.
    # Do not read input or print anything.

    # start from the first element
    cur_sum = nums[0]

    # maintain the min_sum and index of the min_sum
    min_sum = cur_sum
    min_index = 0

    # after calculate the sum, compare it with the min_sum
    for i in range(1, len(nums)):
        # update the cur_sum if the cur_sum is larger than the previous one
        # and the new element is not smaller than the previous sum
        if cur_sum > nums[i]:
            cur_sum = nums[i]

        # if the cur_sum is larger than the min_sum, reset the cur_sum
        # and the index
        if cur_sum > min_sum:
            cur_sum = nums[i]
            min_index = i

        # update the min_sum and the index
        min_sum = min(min_sum, cur
