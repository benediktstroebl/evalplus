import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    # O(n) time | O(1) space
    # if not nums:
    #     return 0

    # min_sum = math.inf
    # running_sum = 0
    # start = 0

    # for i in range(len(nums)):
    #     running_sum += nums[i]
    #     min_sum = min(min_sum, running_sum - nums[start])

    #     if running_sum < 0:
    #         running_sum = 0
    #         start = i + 1

    # return min_sum

    # O(n) time | O(1) space
    if not nums:
        return 0

    min_sum = math.inf
    current_sum = 0

    for num in nums:
        current_sum += num
        min_sum = min(current_sum, min_sum)

        if current_sum < 0:
            current_sum = 0

    return min_sum

