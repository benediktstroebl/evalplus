import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # [2,3,4,1,2,4]
    # 2 3 4 1 2 4
    #   0 3 7 10 12 16
    #       2 3 4 1 2
    #           2 3 4
    #               2
    #                1
    #                   1
    #                       1
    #                           1

    # Step 1: Find the sum of all elements in the array
    sums = 0
    for i in range(len(nums)):
        sums += nums[i]

    # Step 2: Find the sum of the first element
    sumsFirst = nums[0]

    # Step 3: Iterate through the array, keeping track of the current sum and
    # the minimum sum seen so far
    currentSum = 0
    minSum = math.inf

    for num in nums:
        # Step 4: Update the current sum and the minimum sum seen so far
        currentSum += num
        minSum = min(
