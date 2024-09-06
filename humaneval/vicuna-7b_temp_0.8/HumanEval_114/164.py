import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # sort the array
    nums = sorted(nums)
    # initialize the sum to 0 and the current index to 0
    sum = 0
    current = 0
    # initialize the minimum sum
    min_sum = nums[0]
    # check if the array is empty
    if not nums:
        return -1
    # check if the sum of the first two elements is 0
    if nums[0] + nums[1] == 0:
        # check if the sum of the first two elements is 0 and the array is not empty
        if current + nums[1] == 0:
            # update the sum and current index
            sum += nums[1]
            current += 1
            # update the minimum sum
            min_sum = min_sum + nums[1]
        else:
            # update the sum and current index
            sum += nums[1]
            current += 1
            # update the minimum sum
            min_sum = min(min_sum, sum)
    # check if the current index is greater than the length of the array
    while current < len(nums):
        # check if the sum of the current element and the next element is 0
        if current + nums[current + 1] == 0:
            # update the sum and current index
            sum += nums[current + 1]
            current += 2
            # update the minimum sum
            min_sum = min(min_sum, sum)
        else:
            # update the sum and current index
            sum += nums[current + 1]
            current += 2
        # check if the current index is greater than the length of the array
        if current == len(nums) - 1:
            break
    # return the minimum sum
    return min_sum
