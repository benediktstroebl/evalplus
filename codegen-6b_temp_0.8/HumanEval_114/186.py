import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    #TLE
    def minSubArraySum(nums):
        if not nums:
            return None
        min_sum = inf
        sum = 0
        for n in nums:
            sum += n
            min_sum = min(min_sum, sum)
            if sum < 0:
                sum = 0
        return min_sum
    #binary search
    left, right = 0, 0
    left_sum = nums[0]
    while left < len(nums) and left_sum < 0:
        left += 1
        left_sum += nums[left]
    right_sum = nums[-1]
    while right < len(nums) and right_sum < 0:
        right += 1
        right_sum += nums[right]
    if left_sum < 0:
        left_sum = 0
    if right_sum < 0:
        right_sum = 0
    mid = (left + right) // 2
    while left < mid < right:
        mid_sum = nums[mid]
        left_sum = left_sum - nums[left] + nums[mid]
        right_sum = right_sum - nums[right - 1] + nums[mid]
        left += 1
        right -= 1
        if left_sum >= 0 and right_sum >= 0:
            min_sum = min(min_sum, left_sum + right_sum)
        else:
            if left_sum < 0:
                left_sum = 0
            if right_sum < 0:
                right_sum = 0
            min_sum = min(min_sum, left_sum + right_sum)
    return min_sum
