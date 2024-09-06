import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    if not nums:
        return 0

    # storing the sum of the subarray from index 0 to the last index
    sums = [0]
    for i in range(len(nums)):
        sums.append(sums[-1] + nums[i])

    # storing the min sum of the subarray from index 0 to the last index
    min_sums = [sums[0]]
    for i in range(len(sums)):
        # min_sums.append(min(min_sums[-1], sums[i]))
        min_sums.append(min(min(min_sums[-1], sums[i]), sums[i] - sums[0]))

    return min_sums[-1]
