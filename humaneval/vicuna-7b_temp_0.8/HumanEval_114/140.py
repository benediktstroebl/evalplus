import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # 判断是否有负数
    if sum(nums) < 0:
        return -sum(nums)
    # 合併多个相同的数组
    nums = sorted(nums)
    n = len(nums)
    for i in range(1, n):
        for j in range(i, n):
            # 如果两个数相等，则不需要再检查
            if nums[i] == nums[j]:
                continue
            # 如果一个数小于等于另一个数，则检查它们是否一起小于等于0
            if nums[i] < nums[j]:
                min_sum = min(nums[i], nums[j])
                # 如果sum不等于0，则需要进一步检查
                if min_sum != 0:
                    continue
                # 否则，sum等于0，所以这两个数的sum是最小的
                return 0
    return 0