import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # define minSum as a variable to store the minimum sub-array sum
    minSum = 0

    # sum up all array elements, but exclude first element (initial minSum)
    for num in nums:
        minSum += num

    # define currentMin as a variable to store the current minimum sub-array sum
    currentMin = minSum

    # sum up first element and exclude last element
    for i in range(1, len(nums)):
        # update minSum by subtracting last element and adding first element
        minSum = minSum - nums[i-1] + nums[i]

        # update currentMin by comparing it to minSum
        currentMin = min(currentMin, minSum)

    # return the currentMin variable
    return currentMin
