import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    # 1. what is the subarray
    # 2. calculate the sum of subarray
    # 3. return the min subarray sum
    if len(nums) == 0:
        return 0

    min_sum = math.inf
    # use a pair to store the min subarray, the min sum, and the start of the subarray
    min_pair = (None, None, None)
    for i in range(len(nums)):
        # 0 1 2 3 4
        # 1 2 3 4 5
        # 1 2 3 4 5 6
        # 1 2 3 4 5 6 7
        # 1 2 3 4 5 6 7 8
        sub_sum = nums[i]
        start = i
        for j in range(i + 1, len(nums) + 1):
            # 0 1 2 3 4 5
            # 1 2 3 4 5 6
