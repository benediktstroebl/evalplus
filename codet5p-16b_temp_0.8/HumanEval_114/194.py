import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    if len(nums) == 0:
        return 0
    else:
        sub_array_sum = nums[0]
        minimum = math.inf
        for i in range(len(nums)):
            if sub_array_sum < 0:
                sub_array_sum = nums[i]
            else:
                sub_array_sum += nums[i]

            if sub_array_sum < minimum:
                minimum = sub_array_sum

        return minimum
