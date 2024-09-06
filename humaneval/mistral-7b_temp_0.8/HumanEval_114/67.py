import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # 求前面的累加和
    n = len(nums)
    sums = [0]
    for i in range(n):
        sums.append(sums[i] + nums[i])

    min_sum = math.inf
    for i in range(n):
        # 用数组来减小复杂度
        left = i
        right = n - 1
        while left < right:
            sums_in_range = sums[right] - sums[left]
            if sums_in_range < min_sum:
                min_sum = sums_in_range
                if sums_in_range == 0:
                    return i
            if sums[right] - sums[left] > 0:
                right -= 1
            else:
                left += 1
    return -1
