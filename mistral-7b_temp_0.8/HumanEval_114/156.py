import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # 1. 找到最小子数组
    # 2. 找到数组中的最大值
    # 3. 使用二分查找在数组中找到最大值所在的区间
    # 4. 计算区间和
    # 5. 使用二分查找在区间上找到最小的值
    min_sum = 0
    if len(nums) == 0:
        return 0
    left = 0
    right = 0
    min_sum = min(nums)
    while right < len(nums):
        left = right
        sum = 0
        while right < len(nums):
            sum += nums[right]
            min_sum = min(sum, min_sum)
            right += 1
    return min_sum
