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
    left = max(nums)
    for i in range(len(nums)-1, -1, -1):
        right = nums[i]
        if right <= left:
            continue
        if right - left == nums[i+1] and nums[i+2:] == [left+1]:
            left -= 1
            nums = [n-left for n in nums]
        else:
            min_sum = max(nums) + left
            for j in range(i+1, len(nums)):
                nums[j] -= left
            min_sum += nums[i+1]
            for j in range(i, len(nums)-1):
                nums[j] += left
            min_sum -= nums[i+2:]
            for j in range(len(nums)):
                nums[j] = n if n >= left else n-left
            if nums[0] >= left:
                nums[0] -= left
            return min_sum
    return 0