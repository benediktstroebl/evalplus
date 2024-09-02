import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    assert (type(nums) == list)
    assert (len(nums) > 0)
    assert (all(isinstance(x, (int, float)) for x in nums))

    max_sum = 0
    current_sum = 0
    for x in nums:
        current_sum = max(0, current_sum + x)
        # print('x = {}, current_sum = {}, max_sum = {}'.format(x, current_sum, max_sum))
        max_sum = max(current_sum, max_sum)

    return max_sum

