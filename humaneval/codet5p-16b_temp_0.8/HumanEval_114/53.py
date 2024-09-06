import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    sums = [nums[0]]
    minSum = math.inf
    for num in nums[1:]:
        sums.append(sums[-1] + num)
    
    for index in range(len(sums)):
        if sums[index] >= 0:
            for index2 in range(index + 1, len(sums)):
                minSum = min(minSum, sums[index2] - sums[index] + nums[index])
    return minSum if minSum < math.inf else -1
