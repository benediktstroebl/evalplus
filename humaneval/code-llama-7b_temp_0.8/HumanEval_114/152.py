import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # for case when array is empty
    if len(nums) == 0:
        return 0
    elif len(nums) == 1:
        return nums[0]

    # use sliding window with two pointers
    i,j = 0,0
    sum = math.inf
    while j < len(nums):
        # add sum
        sum = sum - nums[i]
        # compare and update min sum
        if sum > 0:
            sum = sum + nums[j]
        if sum < sum:
            sum = sum
        # move right
        j += 1
        if j >= len(nums):
            break
        # move left if sum is greater than 0
        if sum >= 0:
            i = j - 1
    return sum
