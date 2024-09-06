import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    size = len(nums)
    if size == 0:
        return 0
    sumArray = []
    for i in range(size):
        sumArray.append(nums[i])
        for j in range(i + 1, size):
            sumArray.append(sumArray[j - 1] + nums[j])

    result = math.inf
    for item in sumArray:
        if item < result:
            result = item
    return result

