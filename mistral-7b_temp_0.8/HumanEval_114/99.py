import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    # minSum is going to be the answer to this question
    minSum = math.inf

    # numsSums is going to be all the sums we have calculated
    numsSums = [0]

    # We are going to create a sums array and we will update it as we go. This way we can keep track
    # of the sum of each subarray
    for num in nums:
        numsSums.append(numsSums[-1] + num)

    # We are going to keep track of the minSum for the subarray of each index
    minSubarraySum = [0] * len(nums)

    # We will fill in the minSubarraySum array
    for index, num in enumerate(numsSums):
        # The current sum is smaller than the sum of the current index minus the first index
        if num < minSubarraySum[index-1]:
            minSubarraySum[index] = num
        # The current sum is larger than the sum of the current index minus the first index
        else:
            minSubarray
