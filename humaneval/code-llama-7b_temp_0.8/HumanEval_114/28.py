import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    numsLen = len(nums)
    sums = []
    runningSum = 0

    # for each index
    for i in range(0, numsLen):

        # set runningSum
        runningSum += nums[i]

        # add subarray to sums array
        if i > 0:
            sums.append(runningSum - nums[i - 1])

        # if i == 0 then we have to add all of nums to sums
        else:
            sums.append(runningSum)

    return min(sums)

