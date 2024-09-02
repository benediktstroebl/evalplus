import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # -6
    # if len(nums) == 0:
    #     return 0
    # if len(nums) == 1:
    #     return nums[0]
    # if len(nums) == 2:
    #     return min(nums[0], nums[1])
    # if len(nums) == 3:
    #     return min(nums[0], nums[1], nums[2])
    #
    # mid = int(len(nums) / 2)
    # l1 = minSubArraySum(nums[:mid])
    # l2 = minSubArraySum(nums[mid:])
    #
    # l1_sum = l2_sum = 0
    # l1_idx = l2_idx = 0
    # for i in range(len(nums)):
    #     l1_sum += nums[i]
    #     l2_sum += nums[i]
    #     while l1_sum >= l1 and l1_idx < mid:
    #         l1_sum -= nums[l1_idx]
    #         l1_idx += 1
    #     while l2_sum >= l2 and l2_idx < len(nums) - mid:
    #         l2_sum -= nums[l2_idx]
    #         l2_idx += 1
    #     l1 = min(l1, l1_sum)
    #     l2 = min(l2, l2_sum)
    # return min(l1, l2)
    pass

