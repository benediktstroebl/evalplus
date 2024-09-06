import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # write your code here
    if not nums:
        return 0

    _min = nums[0]
    _sum = 0
    for i in range(len(nums)):
        _sum += nums[i]
        if _sum < 0:
            _sum = 0
        elif _sum < _min:
            _min = _sum
    return _min

