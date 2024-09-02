import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    sum = math.inf
    sums = []

    for i in range(0, len(nums)):
        sums.append(nums[i])
        for j in range(i + 1, len(nums)):
            sums.append(sums[-1] + nums[j])
            if sums[-1] < sum:
                sum = sums[-1]
    
    if len(nums) == 1:
        return nums[0]
    return sum

