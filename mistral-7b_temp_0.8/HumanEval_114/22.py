import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # edge case
    if not nums:
        return 0

    # min sum
    min_sum = math.inf

    # min length
    min_length = len(nums) + 1

    # sum
    sum = 0

    for num in nums:
        sum += num
        if sum < min_sum:
            min_sum = sum
            min_length = 1
        elif sum == min_sum:
            min_length += 1
        else:
            # reset sum
            sum = 0

    return min_length


