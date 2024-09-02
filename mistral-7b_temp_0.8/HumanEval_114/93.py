import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # 不断循环找到最小值
    # 找到最小值的时候，要从头开始，因为只要有一个小于当前最小值，就更新
    # 要排除一些情况，如果最大值小于等于0，直接返回0，因为对于负数来说，最小值不可能超过0
    # 如果最小值小于等于0，直接返回0
    min_value = math.inf
    # 用于记录最小值的索引值
    index_min_value = 0
    for i in range(len(nums)):
        nums[i] = nums[i] if nums[i] > 0 else 0
        # print(nums)
        if nums[i] <= min_value:
            # print('一次循环')
            min_value = nums[i]
            index_min_value = i
        if min_value == 0:
            return 0
        if min
